import requests, csv, re
import json

from urls import provide_urls
from utils.headers import json_header, request_headers


def json_request(url, geo, detail, offset, attraction, update_token):
    """ Send a request to get json data """
    cookies, headers, json_data = json_header(url, geo, detail, offset, attraction, update_token)
    response = requests.post('https://www.tripadvisor.com/data/graphql/ids', cookies=cookies, headers=headers, json=json_data, timeout=10)

    return response.json()


def parse_json(json_response):
    """ Retrive required data form the json response """
    content_list = []
    photo = dict()
    json_data = json_response
    reviews = (json_data[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][2:12])

    for review in reviews:
        if review['__typename'] == 'WebPresentation_ReviewsNoFilterResultsCardWeb':
            continue

        title = review['htmlTitle']['text']
        body = review['htmlText']['text']
        date = review['publishedDate']['text']
        name = review['userProfile']['displayName']
        hometown = review['userProfile']['hometown']
        url = review['cardLink']['webRoute']['webLinkUrl']
        images = review['userProfile']['profileImage']['photoSizes']
        
        for index, image in enumerate(images):
            photo = photo | {f'photo{index}': image['url']}

        content_list.append({'title': title, 'body':body, 'date':date, 'name':name, 'hometown':hometown, 'url':url, 'images': photo})

        # currentPageNumber = pr[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][12]['currentPageNumber']
    # try:
    # next_page = pr[3]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'] \
    #                 [0]['content'][12]['links'][1]['updateLink']['webRoute']['webLinkUrl']
        # print('next_page\n')
        # print(next_page) 
        # print('\n\n\n\n')
    # except:
        # next_page = None

    # print(content_list[0])
    # print(next_page)

    return content_list


def get_geo_info(url):
    """ Retrieve info from the url """
    if 'https://www.tripadvisor.com' in url:
        url = url.replace('https://www.tripadvisor.com', '')

    attraction = url.split('/')[1].split('-g')[0]
    offset = 'r10'
    geo = url.split('-g')[1].split('-d')[0]
    detail = url.split('-d')[1].split('-or')[0]
    

    try:
        detail = int(detail)
        detail = str(detail)
    except:
        detail = url.split('-d')[1].split('-')[0]

    try: 
        offset = url.split('-o')[1].split('-')[0]
    except:
        url = '-'.join(url.split('-')[0:3]) + '-or10-' + '-'.join(url.split('-')[3:]) 
        
    return {'geo':geo, 'offset':offset, 'detail':detail, 'attraction':attraction, 'url':url}


def save_csv(cleaned_reviews):
    with open('data.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'body'])
        for _, review in cleaned_reviews.items():
            writer.writerow({'title': review['title'], 'body':review['body']})


def save_json(cleaned_reviews):
    """ Save parsed json data in json file """
    with open('data.json', 'w') as file:
        json.dump(cleaned_reviews, file, indent=4)        


# def handle_process(url, geo, detail, attraction, total_reviews=[], offset='r10'):
    
#     offset_num = int(offset[1:]) + 10
#     offset = 'r' + str(offset_num)
#     # url = url.replace('r80', offset)
#     pattern = r'r\d+'
#     url = re.sub(pattern, offset, url)
#     # print(geo, detail, offset, attraction, url)

#     res = json_request(url, geo, detail, offset, attraction)
#     reviews, next_page = parse_json(res)
#     total_reviews.extend(reviews)

#     print('json_reviews')
#     print(len(total_reviews))

#     # if next_page:
#         # total_reviews = handle_process(url=next_page, geo=geo, detail=detail, attraction=attraction, total_reviews=total_reviews, offset=offset)
    

#     return total_reviews

def check_content(reviews):
    with open('data.json') as file:
        datas = json.load(file)
    
    if datas == reviews:
        return True
    return False

def handle_json(geo_info, update_token=None, total_reviews=[]):
    """ Scrape multiple pages of reviews """

    res = json_request(geo_info['url'], geo_info['geo'], geo_info['detail'], geo_info['offset'], geo_info['attraction'], update_token)
    # print(res[0]['data']['Opf_getOnPageFactorsForLocale'][0]['errMessage'])
    no_of_reviews = res[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][1]['reviewCountText']['text'].split(' ')[0]
    update_token = res[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][12]['links'][2]['updateLink']['updateToken']
    # print(update_token)
    # print(no_of_reviews)
    # print(len(total_reviews))

    # print('\n\n')
    # print(res)
    # print(res[4]['data']['Result'][0]['detailSectionGroups'][0]['detailSections'][0]['tabs'][0]['content'][2:12][0])

    if (int(geo_info['offset'].split('r')[1]) + 10) < (int(no_of_reviews) - 50): 
        reviews = parse_json(res)
        total_reviews.extend(reviews)

        new_offset =  'r' + str(int(geo_info['offset'].split('r')[1]) + 10)
        geo_info['url'] = geo_info['url'].replace(geo_info['offset'], new_offset)
        geo_info['offset'] = new_offset


        total_reviews = handle_json(geo_info, update_token, total_reviews)

    else: 
        print('not running')

    # print('json_reviews\n')
    # print(len(total_reviews))
    # print(f'next_page - {next_page}')

    # if next_page:
    #     total_reviews = handle_json(next_page)
    

    return total_reviews


def scrp_main():
    urls = provide_urls()
    for url in urls:
        geo_info = get_geo_info(url) 
        result = json_request(geo=geo_info['geo'], detail=geo_info['detail'], offset=geo_info['offset'], url=url, update_token=None, attraction=geo_info['attraction'])
        # print(result)
        update_token = result[4]['data']['Result'][0]['detailSectionGroups'][3]['detailSections'][0]['tabs'][0]['content'][12]['links'][1]['updateLink']['updateToken']
        print(update_token)

        result_list = handle_json(geo_info=geo_info, update_token=update_token, total_reviews=[])
    save_json(result_list)


if __name__ == "__main__":
    # get_geo_info('/Attraction_Review-g298570-d447384-Reviews-or10-Chinatown-Kuala_Lumpur_Wilayah_Persekutuan.html')
    scrp_main()    

