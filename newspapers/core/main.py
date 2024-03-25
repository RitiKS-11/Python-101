import csv
import os
import json

from core.sites.himalayan_times import HimalayanTimes
from core.sites.republica import Republica
from core.sites.kathmandu_post import KathmanduPost
from core.analyze import handle_process, convert_to_csv


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
# NEWS_SITES = [HimalayanTimes]

def get_news(keyword):
    for site in NEWS_SITES:
        print(site)
        perform_operation(source=site, keyword=keyword)


def perform_operation(source, keyword):
    try:

        result = source(keyword=keyword, url=None)
        full_path = os.path.join(os.getcwd() + '/' + str(result.__repr__()) + '/' + keyword)

        total_pages = int(result.get_total_page())
        print(total_pages)
        current_page = int(result.get_page(full_path))
        print(current_page)

        for _ in range(current_page, total_pages):
            result.parse_content()

    except Exception as e:
        print(e)

    finally:
        json_to_csv(keyword)


def handle_full_contents(source, keyword):
    try:
        result = source(keyword=keyword)
        result.full_content()
    except Exception as e:
        print(e)

def full_contents_job(keyword):
    for site in NEWS_SITES:
        handle_full_contents(site, keyword)


def full_process(keyword):
    # get_news(keyword)
    # full_contents_job(keyword)
    # handle_process()
    convert_to_csv('processed.json')


        

if __name__ == "__main__":
    # get_news()
    # full_contents_job()
    full_process('Tech')