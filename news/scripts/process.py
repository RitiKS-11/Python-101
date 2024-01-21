import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import FreqDist
from nltk.tag import pos_tag


def tokenize_news(news):
    news_word_list = word_tokenize(news)
    return news_word_list


def remove_stopwords(tokenized_words):
    stop_words = set(stopwords.words("english"))    
    filtered_stopwords = [word for word in tokenized_words if word.casefold() not in stop_words]
    return filtered_stopwords

def remove_punctuation(filtered_stopwords):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    filtered_words = [word for word in filtered_stopwords if word not in punctuation]
    return filtered_words


def get_news():
    with open('news.json') as file:
        results = json.load(file)

    for result in results.items():
        return result[1]['news']
    

def stemming_and_lemmatizing(filtered_words):
    stemmer = PorterStemmer()
    lemmtizer = WordNetLemmatizer()
    stemmed_words = [stemmer.stem(word) for word in filtered_words]
    lemmtized_words = [lemmtizer.lemmatize(word) for word in filtered_words]

    return lemmtized_words


def frequency_distribution(filtered_words):
    freq = FreqDist(filtered_words)
    # freq.plot(20)
    return freq.most_common(50)


def chuncking_and_chinking(filtered_words):
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    chinked_grammar = """
                    Chunk: {<.*>+}
                        }<JJ>{"""

    tagged_words = pos_tag(filtered_words)
    chunk_parser = nltk.RegexpParser(grammar)
    tree = chunk_parser.parse(tagged_words)
    return tree



if __name__ == "__main__":
    result = get_news()
    tokenized_words = tokenize_news(result)
    filtered_stopwords = remove_stopwords(tokenized_words)
    filtered_words = remove_punctuation(filtered_stopwords)
    lemmtized_words = stemming_and_lemmatizing(filtered_words)
    lemmtized_words = nltk.Text(lemmtized_words)
    lemmtized_words.collocations()

    # common_words =frequency_distribution(lemmtized_words)
    # print(common_words)

    # tree = chuncking_and_chinking(lemmtized_words)
    # tree.draw()