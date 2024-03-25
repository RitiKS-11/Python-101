import json, os
from collections import defaultdict
import csv

import dateparser
import spacy



def create_nlp(text):
    nlp = spacy.load('en_core_web_sm')
    content_doc = nlp(text)
    return content_doc


def get_article(filepath):
    with open(filepath) as file:
        result = json.load(file)      
    contents = result['articles']

    return contents


def save_json(filepath, data):
    data = data
    if os.path.isfile(filepath) and os.stat(filepath).st_size != 0:
        with open(filepath, 'r') as file:
            contents = json.load(file)

        data = contents + data

    with open(filepath, 'a') as file:
        json.dump(data, file, indent=4)


def clean_words(text):
    content = create_nlp(text)
    content = [token.text for token in content if not token.is_stop and not token.is_punct]
    cleaned_content = ' '.join(content)
    return cleaned_content
    

def extract_data(content):
    content_doc = create_nlp(content)
    result = defaultdict(list)

    for token in content_doc.ents:
        if token.label_ in ['ORG', 'DATE', 'PERSON', 'GPE']:
            result[token.label_].append(token.text)

    return dict(result)

def get_source(url):
    source = url.split('.')[0].replace('https://','')
    return source



def handle_process():
    file_locations = [
        'himalayantimes/Belt+and+Road+Initiative_content.json', 
        'kathmandupost/Belt and Road Initiative_content.json',
        'republica/Belt and Road Initiative_content.json'
        ]
    
    for location in file_locations:
        contents = get_article(location)
        # content = clean_words(content)
        result_list = list()

        for content in contents:
            new_reuslt = dict()
            result = extract_data(content['content'])

            new_reuslt['url'] = content['url']
            new_reuslt['title'] = content['title']
            new_reuslt['published_date'] = format_datetime(content['published_date'])
            new_reuslt['content'] = content['content']
            new_reuslt['anlayzed'] = reomve_repetative_data(result)
            new_reuslt['source'] = get_source(content['url'])


            # print(new_reuslt)
            # print('\n')
            result_list.append(new_reuslt)
        save_json('processed.json', result_list)


def format_datetime(unformatted_date):
    date = unformatted_date
    date = date.replace('Published:', '').strip()

    formatted_date = dateparser.parse(date).strftime("%Y-%m-%d %H:%M")
    print(formatted_date)
    return formatted_date


def reomve_repetative_data(total_results):
    unique_results = dict()
    for key, values in total_results.items():
        unique_results[key] = list(set(values))

    return unique_results
    
    
def convert_to_csv(filepath):
    with open(filepath) as file:
        results = json.load(file)

    fieldnames = ['url', 'title', 'published_date', 'content', 'analyzed_date', 'analyzed_gpe', 'analyzed_org', 'analyzed_person', 'source']

    filepath = filepath.replace('.json', '.csv')
    with open(filepath, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            
            data = {
                'url': result['url'], 
                'title': result['title'], 
                'published_date': result['published_date'], 
                'content':result['content'], 
                'source': result['source']

            }
            analyzed_dict = {f'analyzed_{key.lower()}':result['anlayzed'][key] for key in result['anlayzed'].keys()}
            data = data | analyzed_dict
            print(data)
            writer.writerow(data)
        


if __name__ == "__main__":
    # handle_process()
    convert_to_csv('/home/ritik/workspace/python-101/newspapers/processed.json')

# Person, organization, location dates