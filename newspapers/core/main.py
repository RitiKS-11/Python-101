import csv

from core.scrape import *

def json_to_csv(site):
    with open(f'{site}.json') as file:
        contents = json.load(file)

    with open(f'{site}.csv', 'w') as file:
        fieldnames = ['title', 'url', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for result in contents['articles']:
            writer.writerow(result)

    
def process():
    result = OnlineKhabar()
    result.parse_content()

def get_results_himalayantimes():
    try:
        result = HimalayanTimes(keyword='bri')
        total_pages = int(result.get_total_page())
        current_page = int(result.get_page('himalayantimes'))
        
        for _ in range(current_page, total_pages):
            print(f'Page no - {_}')
            result.parse_content()
    
    except AttributeError:
        json_to_csv('himalayantimes')


def get_results_republica():
    try:
        result = Republica(keyword='bri')
        total_pages = int(result.get_total_page())
        current_page = int(result.get_page('republica'))

        for _ in range(current_page, total_pages):
            result.parse_content()

    except Exception as e:
        print(e)

    else:
        json_to_csv('republica')

if __name__ == "__main__":
    
    get_results_republica()


    