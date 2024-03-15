import os

from core.scrape import NewsBase

class Republica(NewsBase):
    def __init__(self, keyword, url=None):
        print(keyword)
        self.keyword = keyword
        self.fname = os.path.join(os.getcwd() + '/republica/' + self.keyword)
        self.page = self.get_page(self.fname)

        if url == None:
            self.url = f'https://myrepublica.nagariknetwork.com/news/ajax/query?key={self.keyword}&page={self.page}'
        else:
            self.url = url

        print(self.url)

        headers = {'x-requested-with': 'XMLHttpRequest'}
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

        self.save_data(self.fname, parsed_list, page)

    def get_total_page(self):
        total_page = self.content.json()['template'].split('<li class="disabled">\n                    <span>&hellip;</span>\n                </li>\n                            <li>\n')[-1].split('">')[1].split('</a>\n')[0]
        return int(total_page)
    
    def full_content(self):
        saved_urls = self.get_all_saved_urls(site=self.fname)

        for url in saved_urls:
            url = 'https://myrepublica.nagariknetwork.com' + url
            self.__init__(self.keyword, url=url)
            soup = self.get_soup()

            try:
                title = soup.find('div', class_='main-heading').find('h2').text.strip()
                published_date = soup.find('div', class_='headline-time pull-left').find('p').text.strip().split('By:')[0].split('On:')[1].strip()
                content_elements = soup.find('div', id='newsContent').find_all('p')
                content = ''.join(map(lambda x: x.text, content_elements[:-1]))

                self.fname = self.fname + '_content'

                self.save_data(self.fname, [{'title': title, 'published_date': published_date, 'url': url, 'content': content}], url)       
            except:
                print('except')
                continue

    def __repr__(self):
        return 'republica'
            