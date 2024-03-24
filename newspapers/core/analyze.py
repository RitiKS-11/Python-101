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
    content = result['articles'][0]['content']

    return content


def clean_words(text):
    content = create_nlp(text)
    content = [token.text for token in content if not token.is_stop and not token.is_punct]
    cleaned_content = ' '.join(content)
    return cleaned_content
    

def extract_org_name(content):
    content_doc = create_nlp(content)
    result = defaultdict(list)

    for token in content_doc.ents:
        if token.label_ in ['ORG', 'DATE', 'PERSON', 'GPE']:
            result[token.label_].append(token.text)

    print(result)
    return result


def handle_process():
    content = get_article('himalayantimes/Belt+and+Road+Initiative_content.json')
    # content = clean_words(content)
    extract_org_name(content)


if __name__ == "__main__":
    handle_process()
    

# Person, organization, location dates