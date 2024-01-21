import requests
import re, json
from collections import defaultdict

def get_response(url):
    response = requests.get(url)
    return response

def news_page(response):
    news_list = response.text.split('div class="ssrcss-tq7xfh-PromoContent exn3ah99"><div spacing="2" class="ssrcss-1f3bvyz-Stack e1y4nx260">')[1:]
    results = []

    for news in news_list:
        news_url = news.split('href="')[1].split('" class="ssrcss-its5xf-PromoLink exn3ah91">')[0]
        news_tiltle = news.split('<p class="ssrcss-6arcww-PromoHeadline exn3ah96"><span aria-hidden="false">')[1].split('</span></p></span></a><p class="ssrcss-1q0x1qg-Paragraph e1jhz7w10">')[0]
        
        results.append({'title': news_tiltle, 'url': news_url})

    return results


def scrape_content(response):
    news = response.text.split('<div data-component="text-block" class="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0"><div class="ssrcss-7uxr49-RichTextContainer e5tfeyi1"><p class="ssrcss-1q0x1qg-Paragraph e1jhz7w10"><b class="ssrcss-hmf8ql-BoldText e5tfeyi3">')
    if len(news) >= 2:
        pattern_1 = '</p></div></div><div data-component="topic-list" class="ssrcss-1qmkvfu-TopicListWrapper etw6iwl1">'
        pattern_2 = '&quot;</p></div></div><div data-component="text-block" class="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0"><div class="ssrcss-7uxr49-RichTextContainer e5tfeyi1">'
        
        if pattern_1 in news[1]:
            news = news[1].split(pattern_1)[0]
        elif pattern_2 in news[1]:
            news = news[1].split(pattern_2)[0]

        text_inside_angle_brackets = r'<(.*?)>'
        clean_news = re.sub(text_inside_angle_brackets, '', news)
    
        return {'title': clean_news.split('.')[0], 'news':clean_news}
    return ''

def save_content(news):

    with open('news.json', 'w') as file:
        json.dump(news, file, indent=4)


def handle_scrping(page):
    processed_result = defaultdict(str)
    not_news_list = ['sounds', 'iplayer', 'sport']
    
    while page <= 5:

        res = get_response(f"https://www.bbc.co.uk/search?q=apple&d=SEARCH_PS&seqId=undefined&page={page}")
        results = news_page(res)

        for result in results:
            url = result['url']
            title = result['title']
            if all(not_news not in url for not_news in not_news_list) and  'bbc.co.uk' in url:
                print(title, url)

                res = get_response(url)
                news = scrape_content(res)


                processed_result[title] = news

        
        page += 1


    save_content(processed_result)


if __name__ == "__main__":
    handle_scrping(1)
    # res = get_response('https://www.bbc.com/news/world-asia-india-67634680')
    # result = scrape_content(res)
    # print(result)