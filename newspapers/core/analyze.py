import spacy
from spacy.matcher import Matcher
import json
from collections import defaultdict

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
    with open(filepath, 'w') as file:
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


def handle_process():
    contents = get_article('himalayantimes/Belt+and+Road+Initiative_content.json')
    # content = clean_words(content)
    total_results = dict()

    for content in contents:
        result = extract_data(content['content'])

        keys = set(total_results.keys()) | set(result.keys())
        for key in keys:
            if key in total_results.keys() and key in result.keys():
                total_results[key] = total_results[key] + result[key]
            elif key in result:
                total_results[key] = result[key]

    total_results = reomve_repetative_data(total_results)
    save_json('processed.json', total_results)


def reomve_repetative_data(total_results):
    unique_results = dict()
    for key, values in total_results.items():
        unique_results[key] = list(set(values))

    return unique_results
    
    


if __name__ == "__main__":
    handle_process()
    

# Person, organization, location dates