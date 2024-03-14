from core.scrape import NewsBase

class Republica(NewsBase):
    def __init__(self, keyword='tech'):
        self.keyword = keyword
        self.page = self.get_page('Republica')
        self.url = f'https://myrepublica.nagariknetwork.com/news/ajax/query?key={self.keyword}&page={self.page}'

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

        self.save_data('Republica', parsed_list, page)

    def get_total_page(self):
        total_page = self.content.json()['template'].split('<li class="disabled">\n                    <span>&hellip;</span>\n                </li>\n                            <li>\n')[-1].split('">')[1].split('</a>\n')[0]
        return int(total_page)