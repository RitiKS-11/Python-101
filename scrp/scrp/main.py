import requests, csv, re
import json

from urls import provide_urls
from utils.headers import json_header, request_headers

index = 0

def get_page(url):
    try:
        cookies, headers = request_headers()

        response = requests.get(
            url,
            cookies=cookies,
            headers=headers,
            timeout=10
        )
        # print(response.text)
        return response.text

    except Exception as e:
        print(e)
        raise e
    

def parse_content(response):
    parsed_content_list = list()
    next_page = ''

    content = response.split('<span class="biGQs _P fiohW fOtGX"><a target="_self" href="/Profile/ianb111" class="BMQDV _F Gv wSSLS SwZTJ FGwzt ukgoS">ianb111</a></span><div class="JINyA"><div class="biGQs _P pZUbB osNWb"><span>')[-1].split('<div class="HdolS"></div><div class="xkSty">')
    next_page_count = content[-1].split('<div class="UCacc"><a class="BrOJk u j z _F wSSLS tIqAi unMkR" data-smoke-attr="pagination-next-arrow" aria-label="Next page" href="')

    if not len(next_page_count)<=1:
        next_page = next_page_count[1].split('"><svg viewBox="0 0 24 24" width="24px" height="24px" class="d Vb UmNoP">')[0]
        
    reviews = content[0].split('<div class="biGQs _P fiohW qWPrE ncFvv fOtGX">')[1:]

    for review in reviews:
        title = review.split('<span class="yCeTE">')[1].split('</span></a></div><div class="RpeCd">')[0]
        date = len(review.split('</div><div class="RpeCd">'))
        if date >= 2:
            review_date = review.split('</div><div class="RpeCd">')[1].split('</div><div class="_T FKffI bmUTE">')[0]
        else:
            review_date = ''
        review_body = review.split('<span class="JguWG"><span class="yCeTE">')[1].split('</span></span></div></div><div class="lszDU">')[0]
        parsed_content_list.append({'title': title,  'body': review_body, 'date':review_date})    
    
    print(next_page)
    print('\n')
    return (parsed_content_list, next_page)


def json_request(url, geo, detail, offset, attraction):
    cookies, headers, json_data = json_header(url, geo, detail, offset, attraction)
    response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data)

    return response.json()


def parse_json(json_response):
    content_list = []
    pr = json_response
    # print(pr)
    reviews = (pr[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][2:12])
    for review in reviews:
        print(review)
        print('\n\n\n\n\n')

        if review['__typename'] == 'WebPresentation_ReviewsNoFilterResultsCardWeb':
            continue

        title = review['htmlTitle']['text']
        body = review['htmlText']['text']
        date = review['publishedDate']['text']

        content_list.append({'title': title, 'body':body, 'date':date})

        currentPageNumber = pr[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][12]['currentPageNumber']
        next_page = pr[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][12]['links'][2]['internalLink']['webRoute']['webLinkUrl']
        print(next_page)

    return content_list


def get_geo_info(url):
    attraction = url.split('/')[1].split('-g')[0]

    # attraction = 'attraction' if attraction == 'Attraction' else 'attraction_product'
    geo = url.split('-g')[1].split('-d')[0]
    detail = url.split('-d')[1].split('-or')[0]
    offset = url.split('-o')[1].split('-')[0]

    return (geo, detail, offset, attraction)


def clean_content(content_list):
    updated_contet_list = list()
    PATTERN = '\<[^>]*\>'
    
    for item in content_list:
        item['title'] = re.sub(PATTERN, '', item['title'])
        item['date'] = item['date'].replace('<br />', '')
        item['body'] = re.sub(PATTERN, '', item['body'])
        updated_contet_list.append(item)

    return updated_contet_list


def save_csv(cleaned_reviews):
    with open('data.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'body'])
        for _, review in cleaned_reviews.items():
            writer.writerow({'title': review['title'], 'body':review['body']})


def save_json(cleaned_reviews):
    with open('data.json', 'w') as file:
        json.dump(cleaned_reviews, file, indent=4)        


def handle_process(urls, total_reviews=[]):
    global index
    for url in urls:
        response = get_page(url)
        content_list, next_page = parse_content(response)
        cleaned_reviews = clean_content(content_list)

        total_reviews = total_reviews + cleaned_reviews
        print(len(total_reviews))

        if next_page:
            print(f'Next page {index}')
            index += 1
            geo, detail, offset, attraction = get_geo_info(next_page)
            res = json_request(next_page, geo, detail, offset, attraction)
            reviews = parse_json(res)
            total_reviews = total_reviews + reviews

    return total_reviews


def scrp_main():
    urls = provide_urls()
    result_list = handle_process(urls)
    save_json(result_list)


if __name__ == "__main__":
    # get_geo_info('/Attraction_Review-g298570-d447384-Reviews-or10-Chinatown-Kuala_Lumpur_Wilayah_Persekutuan.html')
    scrp_main()    

