import requests, os
from bs4 import BeautifulSoup
import json
from datetime import datetime

class NewsBase:
    def __init__(self, url='', keyword='tech'):
        self.url = url
        self.keyword = keyword

    def get_response(self):
        response= requests.get(self.url, timeout=10)
        return response
    
    def create_soup(self, response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        return soup
    
    def save_data(self, site, data, page):
        contents = dict()
        filename = site + '.json'

        if os.path.isfile(filename) and os.stat(filename).st_size != 0:
            with open(filename, 'r') as file:
                contents = json.load(file)

            contents['articles'] = contents['articles'] + data
            contents['current_page'] = page
        else:
            contents['articles'] = data
            contents['current_page'] = page


        with open(filename, 'w') as file:
            json.dump(contents, file, indent=4)

    def get_page(self, site):
        filename = site + '.json'

        if os.path.isfile(filename) and os.stat(filename).st_size != 0:

            with open(filename, 'r') as file:
                contents = json.load(file)
                
                if 'current_page' in contents.keys():
                    return contents['current_page']
                return 1
        return 1    
        

class HimalayanTimes(NewsBase):
    def __init__(self, url=''):
        super().__init__()
        self.page_no = self.get_page('himalayantimes')
        self.url = f'https://thehimalayantimes.com/search?query={self.keyword}&pgno={self.page_no}'
        self.data = {}

    def parse_content(self):
        parsed_list = []
        self.content = self.get_response()
        self.soup = self.create_soup(self.content.text)

        current_page = self.soup.find('li', class_='pager-nav active').text
        articles = self.soup.find_all('article', class_='row animate-box fadeInUp animated-fast')

        for article in articles:
            title = article.find('h3', class_='alith_post_title').text
            url = article.find('h3', class_='alith_post_title').find('a')['href']
            description = article.find('div', class_='alith_post_except').text.strip().replace('\n','')

            parsed_list.append({'title': title, 'description': description, 'url': url})

        self.data = parsed_list
        self.save_data('himalayantimes',self.data, int(current_page) + 1)

    def next(self):
        # print(self.next_page)
        self.url = self.next_page
        print(self.url)
        self.parse_content()


class RatoPati(NewsBase):
    def __init__(self):
        super().__init__()
        self.page = self.get_page('ratopati')
        self.url = f'https://english.ratopati.com/search?query={self.keyword}&page={self.page}'
        self.data = {}

    def parse_content(self):
        parsed_list = []
        self.content = self.get_response()
        self.soup = self.create_soup(self.content.text)

        articles = self.soup.find_all('article', class_='post-card post-card__more-secondary alternate')
        current_page = self.soup.find('li', class_='page-item active').text

        for article in articles:
            title = article.find('h3', class_='post-card__title').text.strip().replace('\n','')
            url = article.find('h3', class_='post-card__title').find('a')['href']
            description = article.find('div', class_='article-excerpt-default__teaser').text.strip().replace('\n','')

            parsed_list.append({'title': title, 'description': description, 'url': url})

        print(parsed_list)

        self.data = parsed_list
        self.save_data('ratopati', self.data, int(current_page) + 1)




