import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
# from nltk.book import text7
from nltk import FreqDist


STRING = """Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers 
         and humans using natural language. NLTK, or the Natural Language Toolkit, is a powerful library in Python for working with  
         human language data. In this text, we'll explore tokenizing, filtering stop words, stemming, tagging parts of speech, 
         lemmatizing, chunking, chinking, and using Named Entity Recognition (NER) to gain insights from the given content. 
         Additionally, we'll learn how to get text for analysis, use concordance, make dispersion plots, create frequency 
         distributions, and find collocations. NLTK provides a comprehensive set of tools for text processing and analysis."""


def tokenize():
    words = word_tokenize(STRING)
    sentes = sent_tokenize(STRING)

    # print(words)
    # print(sentes)
    return words


def remove_stopwords(words):
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    return filtered_words


def stem(filtered_words):
    stemmer = PorterStemmer()
    stemed_words = [stemmer.stem(word) for word in filtered_words]
    return stemed_words


def lemmatizing(filtered_words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    return lemmatized_words


def tag_pos(filtered_words):
    tagged_post_words = nltk.pos_tag(filtered_words)
    return tagged_post_words


def chuncking(tagged_post_words):
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    chucks = nltk.RegexpParser(grammar)
    tree = chucks.parse(tagged_post_words)
    return tree

def chunk_and_chink(tagged_post_words):
    grammar = """
        Chunk: {<.*>+}
            }<JJ>{"""
    
    chunks_chinks = nltk.RegexpParser(grammar)
    tree = chunks_chinks.parse(tagged_post_words)
    return tree

def ner(tagged_post_words):
    tree = nltk.ne_chunk(tagged_post_words)
    return tree


# def dispersion():
#     text7.dispersion_plot(["same", "right", "next", "first", "hard", "short"])


def frequency(filtered_words):
    freq = FreqDist(filtered_words)
    # freq.plot(20, cumulative=True)

    return freq.most_common(20)


def collocations(text7):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in text7]
    new_text = nltk.Text(lemmatized_words)
    return new_text.collocations()


def get_synonym_and_antonym(word):
    syns = wordnet.synsets(word)
    # print(syns)
    synonyms = []
    antonyms = []

    for syn in syns:
        for lem in syn.lemmas():
            synonyms.append(lem.name())
            if lem.antonyms():
                antonyms.append(lem.antonyms()[0].name())
    
    #definition 
    print(syns[0].definition())

    #example
    print(syns[3].examples())

    return (synonyms, antonyms)

if __name__ == "__main__":
    syno, anto = get_synonym_and_antonym("High")

    print("Synonyms: ", syno)
    print("Antonyms: ", anto)

    