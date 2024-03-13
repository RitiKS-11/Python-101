import requests, os
import csv
from bs4 import BeautifulSoup
import json
from pprint import pprint

class NewsBase:
    def __init__(self, url='', keyword='tech'):
        self.url = url
        self.keyword = keyword

    def get_response(self, headers=''):
        response= requests.get(self.url, timeout=10, headers=headers)
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
    def __init__(self, keyword):
        self.keyword = keyword
        super().__init__(keyword=self.keyword)
        self.page_no = self.get_page('himalayantimes')
        self.url = f'https://thehimalayantimes.com/search?query={self.keyword}&pgno={self.page_no}'
        print(self.url)
        self.data = {}
        self.content = self.get_response()
        self.soup = self.create_soup(self.content.text)


    def parse_content(self):
        parsed_list = []
        
        self.__init__(self.keyword)

        current_page = self.soup.find('li', class_='pager-nav active').text
        current_page = int(current_page) + 1
        articles = self.soup.find_all('article', class_='row animate-box fadeInUp animated-fast')
        
        for article in articles:
            title = article.find('h3', class_='alith_post_title').text
            url = article.find('h3', class_='alith_post_title').find('a')['href']
            description = article.find('div', class_='alith_post_except').text.strip().replace('\n','')

            parsed_list.append({'title': title, 'description': description, 'url': url})

        self.data = parsed_list
        self.save_data('himalayantimes',self.data, current_page)

    def get_total_page(self):
        total_page = int(self.soup.find_all('li', class_='pager-nav')[-2].text)
        return total_page

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


class SetoPati(NewsBase):
    def __init__(self):
        super().__init__()
        self.page = self.get_page('setopati')
        self.url = f'https://en.setopati.com/search?keyword={self.keyword}&page={self.page}'

    def parse_content(self):
        parsed_list = []

        self.content = self.get_response()
        self.soup = self.create_soup(self.content.text)

        articles = self.soup.find_all('div', class_='items col-md-4')
        current_page = self.soup.find('span', class_='current').text

        for article in articles:
            title = article.find('a').text.replace('\n','').strip
            url = article.find('a')['href']

            parsed_list.append({'title': title, 'url': url})

        self.save_data('setopati', parsed_list, int(current_page) + 1)


class OnlineKhabar(NewsBase):
    def __init__(self):
        super().__init__()
        self.page = self.get_page('onlinekhabar')
        self.url = f'https://english.onlinekhabar.com/page/{self.page}?s={self.keyword}'

    def parse_content(self):
        parsed_list = []

        content = self.get_response()
        soup = self.create_soup(content.text)

        articles = soup.find_all('div', class_='ok-news-post ltr-post')
        current_page = soup.find('span', class_='page-numbers current').text

        for ariticle in articles:
            title = ariticle.find('h2').find('a').text.replace('\n','').strip()
            url = ariticle.find('h2').find('a')['href']

            parsed_list.append({'title': title, 'url': url})

        self.save_data('onlinekhabar', parsed_list, int(current_page)+1)


class NepalKhabar(NewsBase):
    def __init__(self):
        super().__init__()
        self.page = self.get_page('nepalkhabar')
        self.url = f'https://en.nepalkhabar.com/search/{self.keyword}?page={self.page}'

    def parse_content(self):
        parsed_list = []

        content = self.get_response()
        soup = self.create_soup(content.text)

        articles = soup.find_all('div', class_='uk-grid-margin uk-first-column')
        current_page = soup.find('li', class_='uk-active')

        for article in articles:
            title = article.find('a', class_='uk-link-heading').text.strip().replace('\n','')
            url = article.find('a', class_='uk-link-heading')['href']

            parsed_list.append({'title': title, 'url': url})

        self.save_data('nepalkhabar', parsed_list, int(current_page)+1)


class Republica(NewsBase):
    def __init__(self, keyword='tech'):
        self.keyword = keyword
        self.page = self.get_page('republica')
        print(f'Page - {self.page}')
        self.url = f'https://myrepublica.nagariknetwork.com/news/ajax/query?key={self.keyword}&page={self.page}'

        print(self.url)
        headers = {
            'x-requested-with': 'XMLHttpRequest',
        }
        self.content = self.get_response(headers)

    def parse_content(self):
        parsed_list = []
        self.__init__(self.keyword)

        articles = self.content.json()['template'].split('<h4>')[1:]
        
        for article in articles:
            url = article.split('<a href="')[1].split('/"><u>')[0]
            title = article.split('/"><u>')[1].split('</u></a>')[0]
            description = article.split('<p class="text-default">')[1].split('</p>')[0]

            parsed_list.append({'title':title, 'url':url, 'description':description})

        page = article.split('<li class="active">\n                <span>')[1].split('</span>\n')[0]
        page = int(page) + 1

        self.save_data('republica', parsed_list, page)

    def get_total_page(self):
        total_page = self.content.json()['template'].split('<li class="disabled">\n                    <span>&hellip;</span>\n                </li>\n                            <li>\n')[-1].split('">')[1].split('</a>\n')[0]
        return int(total_page)


class KathmanduPost(NewsBase):
    def __init__(self, keyword):
        self.keyword = keyword
        self.page = int(self.get_page('kathmandupost')) * 10
        self.url = f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={self.page}&cselibv=8435450f13508ca1&cx=006439178574289969438%3A21nndnycfqd&q={self.keyword}&safe=off&cse_tok=AB-tC_6-V-nvygNNStnMjuvkL9EY%3A1710327425779&sort=&exp=cc%2Cnpo%2Cdtsq-3&fexp=72519161%2C72519164&callback=google.search.cse.api8080'
        print(self.page)
        self.response = self.get_response()
        response = str(self.response.text)
        new = response.replace('/*O_o*/', ''). \
                        replace('google.search.cse.api8080(',''). \
                        replace(');', '')
        self.json_response = json.loads(new)

    def parse_content(self):
        parsed_list = []
        
        self.__init__(self.keyword)
        articles = self.json_response['results']
        page = int(self.json_response['cursor']['currentPageIndex'])

        for article in articles:
            title = article['titleNoFormatting']
            description = article['contentNoFormatting']
            url = article['url']

            parsed_list.append({'title': title, 'url': url, 'description':description})

        page = int(page) + 1
        self.save_data('kathmandupost', parsed_list, page)

    def get_total_page(self):
        total_page = self.json_response['cursor']['pages'][9]['start']
        return total_page
