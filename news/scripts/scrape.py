import requests
import re, json

def get_response(url):
    response = requests.get(url)
    return response


def scrape_content(response):
    news = response.text.split('<div class="ssrcss-1u2in0b-Container-ContributorDetails e8mq1e913"><div class="ssrcss-68pt20-Text-TextContributorName e8mq1e96">By Yolande Knell</div><div class="ssrcss-84ltp5-Text e8mq1e910">BBC News Middle East correspondent</div></div></div></div><div class="ssrcss-jlwt2c-Divider e8mq1e915"></div></div><div data-component="text-block" class="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0"><div class="ssrcss-7uxr49-RichTextContainer e5tfeyi1"><p class="ssrcss-1q0x1qg-Paragraph e1jhz7w10"><b class="ssrcss-hmf8ql-BoldText e5tfeyi3">')[1].split('</p></div></div><div data-component="topic-list" class="ssrcss-1qmkvfu-TopicListWrapper etw6iwl1">')[0]
    text_inside_angle_brackets = r'<(.*?)>'
    clean_news = re.sub(text_inside_angle_brackets, '', news)
   
    return {'title': clean_news.split('.')[0], 'news':clean_news}

def save_content(news):

    with open('news.json', 'a') as file:
        json.dump(news, file)


if __name__ == "__main__":
    res = get_response("https://www.bbc.com/news/world-middle-east-68034722")
    news = scrape_content(res)
    save_content(news)