import requests, os
from bs4 import BeautifulSoup
import json
from datetime import datetime

class NewsBase:
    def __init__(self, url=''):
        self.url = url

    def get_response(self):
        response= requests.get(self.url, timeout=10)
        return response
    
    def create_soup(self, response_text):
        soup = BeautifulSoup(response_text, 'html.parser')
        return soup
    
    def save_data(self, site, data, page):
        contents = dict()
        if os.path.isfile(site+'.json'):
            with open(site+'.json', 'r') as file:
                contents = json.load(file)

            contents['articles'] = contents['articles'] + data
            contents['current_page'] = page
        else:
            contents['articles'] = data
            contents['current_page'] = page


        # filename = site + datetime.now().strftime('%c').replace(' ','_') + '.json'
        with open(site+'.json', 'w') as file:
            json.dump(contents, file, indent=4)

    def get_page(self, site):
        if os.path.isfile(site+'.json'):
            with open(site+'.json', 'r') as file:
                contents = json.load(file)
                
                if 'current_page' in contents.keys():
                    return contents['current_page']
                return 1
        return 1    
        

class HimalayanTimes(NewsBase):
    def __init__(self, url=''):
        self.page_no = self.get_page('himalayantimes')
        self.url = f'https://thehimalayantimes.com/search?query=job&pgno={self.page_no}'
        self.data = {}

    def parse_content(self):
        parsed_list = []
        self.content = self.get_response()
        self.soup = self.create_soup(self.content.text)

        current_page = self.soup.find('li', class_='pager-nav active').text
        print(current_page)
        # self.next_page = self.soup.find_all('li', class_='pager-nav')[int(self.current_page)+1].find('a')['href']
        articles = self.soup.find_all('article', class_='row animate-box fadeInUp animated-fast')

        for article in articles:
            tilte = article.find('h3', class_='alith_post_title').text
            url = article.find('h3', class_='alith_post_title').find('a')['href']
            description = article.find('div', class_='alith_post_except').text.strip().replace('\n','')

            parsed_list.append({'title': tilte, 'description': description, 'url': url})

        self.data = parsed_list


        
        print(len(self.data))

        self.save_data('himalayantimes',self.data, int(current_page) + 1)

    def next(self):
        # print(self.next_page)
        self.url = self.next_page
        print(self.url)
        self.parse_content()


def process():
    result = HimalayanTimes()
    result.parse_content()
    # result.next()

if __name__ == "__main__":
    process()
 