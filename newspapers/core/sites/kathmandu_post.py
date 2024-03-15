import json, os
from core.scrape import NewsBase


class KathmanduPost(NewsBase):
    def __init__(self, keyword, url=None):
        self.keyword = keyword
        self.fname = os.path.join(os.getcwd() + '/kathmandupost/' + self.keyword)
        self.page = int(self.get_page(self.fname)) * 10


        if url == None:
            self.url = f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={self.page}&cselibv=8435450f13508ca1&cx=006439178574289969438%3A21nndnycfqd&q={self.keyword}&safe=off&cse_tok=AB-tC_6xsIFfHEHcTqkC2KmrN7aS%3A1710484884359&sort=&exp=cc%2Cpos%2Cdtsq-3&fexp=72519171%2C72519168&callback=google.search.cse.api3868'
        else:
            self.url = url


    def parse_content(self):
        parsed_list = []

        self.__init__(self.keyword)

        self.response = self.get_response()
        response = str(self.response.text)
        new = response.replace('/*O_o*/', ''). \
                        replace('google.search.cse.api3868(',''). \
                        replace(');', '')
        self.json_response = json.loads(new)

        articles = self.json_response['results']
        page = int(self.json_response['cursor']['currentPageIndex'])

        for article in articles:
            title = article['titleNoFormatting']
            description = article['contentNoFormatting']
            url = article['url']

            parsed_list.append({'title': title, 'url': url, 'description':description})

        page = int(page) + 1
        self.save_data(self.fname, parsed_list, page)

    def get_total_page(self):
        total_page = self.json_response['cursor']['pages'][9]['start']
        return total_page

    def full_content(self):
        saved_urls = self.get_all_saved_urls(site=self.fname)

        for url in saved_urls:
            print(url)
            self.__init__(keyword=self.keyword, url=url)
            soup = self.get_soup()

            published_date = soup.find('div', class_='updated-time').text
            title = soup.find_all('h1')[-1].text
            content_elements = soup.find('section', class_='story-section')
            content = ''.join(map(lambda x:x.text, content_elements))

        
            self.fname = self.fname + '_content'

            self.save_data(self.fname, [{'title': title, 'published_date': published_date, 'url': url, 'content': content}], url)  

    def __repr__(self):
        return 'kathmandupost'