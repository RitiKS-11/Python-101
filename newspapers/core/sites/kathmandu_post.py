import json
from core.scrape import NewsBase


class KathmanduPost(NewsBase):
    def __init__(self, keyword):
        self.keyword = keyword
        self.page = int(self.get_page('KathmanduPost')) * 10

        self.url = f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=en&source=gcsc&gss=.com&start={self.page}&cselibv=8435450f13508ca1&cx=006439178574289969438%3A21nndnycfqd&q={self.keyword}&safe=off&cse_tok=AB-tC_6-V-nvygNNStnMjuvkL9EY%3A1710327425779&sort=&exp=cc%2Cnpo%2Cdtsq-3&fexp=72519161%2C72519164&callback=google.search.cse.api8080'

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
        self.save_data('KathmanduPost', parsed_list, page)

    def get_total_page(self):
        total_page = self.json_response['cursor']['pages'][9]['start']
        return total_page
