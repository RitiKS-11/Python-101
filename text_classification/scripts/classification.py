import csv, sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

csv.field_size_limit(sys.maxsize)


def get_datas(filepath):
    results = []
    with open(filepath) as file:
        reader = csv.DictReader(file)
        next(reader)
        results = [(word_tokenize(line['email']), line['label']) for line in reader]

    return results


def get_common_words(results):
    all_words = []
    for word_list, label in results:
        for word in word_list:
            all_words.append(word.lower())

    freq_dist = nltk.FreqDist(all_words)
    common_words = freq_dist.most_common(2500)

    return [word for word, _ in common_words]


def clean_text(words_list):
    cleaned_text = []
    stop_words = set(stopwords.words('english'))
    for word in words_list:
        if word not in stop_words:
            word = remove_punctuations(word)
            cleaned_text.append(word)

    return cleaned_text


def remove_punctuations(word):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if type(word) == float:
        return word
   
    text = ''
    for letter in word:
        if letter not in punctuation:
            text += letter
    return text


def get_featureset(email, common_words):
    words = set(email)
    features = {}
    for word in common_words:
        features[word] = (word in words)

    return features


def handle_process(filepath):
    results = get_datas(filepath)
    cleaned_reuslt = []

    for word_list, label in results:
        cleaned_reuslt.append((clean_text(word_list), label))

    common_words = get_common_words(cleaned_reuslt)
    features = [(get_featureset(email, common_words), label) for (email, label) in cleaned_reuslt]

    training_set = features[:1900]
    testing_set = features[1903:]
    
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print("Classifier accuracy:",(nltk.classify.accuracy(classifier, testing_set))*100)


if __name__ == "__main__":
    handle_process("spam_or_not_spam.csv")
