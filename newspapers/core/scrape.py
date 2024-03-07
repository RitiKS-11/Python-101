import requests
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
    
    def save_data(self, site, data):
        filename = site + datetime.now().strftime('%c').replace(' ','_') + '.json'
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
            

class HimalayanTimes(NewsBase):
    def __init__(self):
        self.url = 'https://thehimalayantimes.com/search?query=job'

    def parse_content(self):
        parsed_list = []
        content = self.get_response()
        soup = self.create_soup(content.text)
        
        articles = soup.find_all('article', class_='row animate-box fadeInUp animated-fast')

        for article in articles:
            tilte = article.find('h3', class_='alith_post_title').text
            url = article.find('h3', class_='alith_post_title').find('a')['href']
            description = article.find('div', class_='alith_post_except').text.strip().replace('\n','')

            parsed_list.append({'title': tilte, 'description': description, 'url': url})

        self.save_data('himalayantimes',parsed_list )


def process():
    result = HimalayanTimes()
    result.parse_content()

if __name__ == "__main__":
    process()