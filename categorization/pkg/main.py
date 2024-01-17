import csv
from collections import defaultdict

from pkg.cleanup import clean_data


def get_notes(filepath):
    fields = ['domain', 'federal agency', 'level of government', 'location', 'status', 'note', 'link', 'date added']

    with open(filepath, newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, fieldnames=fields)
        next(reader)       
        notes = [row['note'].split('--')[0] for row in reader]
        
    return notes


def ngrams(sentence, ngram):
    words = sentence.split()
    result = [' '.join(words[i:i+ngram]) for i in range(len(words)-ngram+1)]
    return result


def check_category(ngrams, note_category):
    found_category = defaultdict(int)
    result  = ''
    for word in ngrams:
        for category in note_category:
            categories = category.split(' ')
            words = word.split(' ')

            if any(word in categories for word in words):
                found_category[category] += 1

    
    if found_category:
        result = list(sorted(found_category.items(), key=lambda item: item[1], reverse=True))[:1]
        return result[0][0]
    return 'Undefined'

def top(notes, n):
    ngram = []
    top_words = defaultdict(int)

    for note in notes:
        ngram += ngrams(note, n) 

    for word in ngram:
        if word != '':
            top_words[word] += 1

    sorted_result = dict(sorted(top_words.items(), key=lambda item: item[1], reverse=True))
    top_20 = dict(list(sorted_result.items())[:10])
    return top_20

def write_data(note, note_category):
    with open('note-category.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['category', 'note'])
        writer.writerow({'category':note_category, 'note':note})
    

def main(filepath):

    notes = get_notes(filepath)
    cleaned_notes = clean_data(notes)
    note_category = top(cleaned_notes, 2)

    for index, note in enumerate(cleaned_notes):
        ngram = ngrams(note, 3)
        result_category = check_category(ngram, note_category)
        write_data(notes[index], result_category)


    


if __name__ == "__main__":
    main('3_govt_urls_state_only.csv')