import csv
import os
import json

from core.sites.himalayan_times import HimalayanTimes
from core.sites.republica import Republica
from core.sites.kathmandu_post import KathmanduPost


def json_to_csv(site):
    if os.path.isfile(f'{site}.json'):
        with open(f'{site}.json') as file:
            contents = json.load(file)

        with open(f'{site}.csv', 'w') as file:
            fieldnames = ['title', 'url', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            for result in contents['articles']:
                writer.writerow(result)

    
NEWS_SITES = [HimalayanTimes, Republica, KathmanduPost]

def get_news():
    for site in NEWS_SITES:
        perform_operation(source=site, keyword='nepal')
        break

def perform_operation(source, keyword):
    try:

        result = source(keyword=keyword, url=None)
        full_path = os.path.join(os.getcwd() + '/' + str(result.__repr__()) + '/' + keyword)

        total_pages = int(result.get_total_page())
        current_page = int(result.get_page(full_path))

        for _ in range(current_page, total_pages):
            result.parse_content()

    except Exception as e:
        print(e)

    finally:
        json_to_csv(keyword)
        

if __name__ == "__main__":
    get_news()

    # r = HimalayanTimes('nepal')
    # urls = r.get_full_content()
    # print(len(urls))
    # print(urls)