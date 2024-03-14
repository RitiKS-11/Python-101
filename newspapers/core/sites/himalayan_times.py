import os

from core.scrape import NewsBase

class HimalayanTimes(NewsBase):
    def __init__(self, keyword, url=None):
        self.keyword = keyword
        self.fname = os.path.join(os.getcwd() + '/himalayantimes/' + self.keyword)
        self.page_no = self.get_page(self.fname)

        if url == None:
            self.url = f'https://thehimalayantimes.com/search?query={self.keyword}&pgno={self.page_no}'
        else:
            self.url = url

        print(self.url)
        self.soup = self.get_soup()
        
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
        print('here')
        self.save_data(self.fname, parsed_list, current_page)

    def get_total_page(self):
        total_page = int(self.soup.find_all('li', class_='pager-nav')[-2].text)
        return total_page
    
    def get_full_content(self):
        saved_urls = self.get_all_saved_urls(site=self.fname)

        for url in saved_urls:
            self.__init__(self.keyword, url=url)
            soup = self.get_soup()
            
            title = soup.find('h1', class_='alith_post_title').text.strip()
            published_date = soup.find('div', class_='article_date').text
            content_elements = soup.find('div', class_='post-content').find_all('p')
            content = ''.join(map(lambda x: x.text, content_elements[1:]))

            self.fname = self.fname + '_content'

            self.save_data(self.fname, [{'title': title, 'published_date': published_date, 'url': url, 'content': content}], url)       

    def __repr__(self):
        return 'himalayantimes'