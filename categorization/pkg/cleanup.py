STOPWORDS = ["a", "about", "above", "after", "again", "against", "all", "am", 
             "an", "and", "any", "are", "aren't", "as", "at", "be", "because", 
             "been", "before", "being", "below", "between", "both", "but", "by", 
             "can't", "cannot", "could", "couldn't", "did", "didn't", "do", 
             "does", "doesn't", "doing", "don't", "down", "during", "each", 
             "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", 
             "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", 
             "here", "here's", "hers", "herself", "him", "himself", "his", "how", 
             "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", 
             "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", 
             "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", 
             "once", "only", "or", "other", "ought", "our", "ours	ourselves", 
             "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", 
             "she's", "should", "shouldn't", "so", "some", "such", "than", 
             "that", "that's", "the", "their", "theirs", "them", "themselves", 
             "then", "there", "there's", "these", "they", "they'd", "they'll", 
             "they're", "they've", "this", "those", "through", "to", "too", 
             "under", "until", "up", "very", "was", "wasn't", "we", "we'd", 
             "we'll", "we're", "we've", "were", "weren't", "what", "what's", 
             "when", "when's", "where", "where's", "which", "while", "who", 
             "who's", "whom", "why", "why's", "with", "won't", "would", 
             "wouldn't", "you", "you'd", "you'll", "you're", "you've", 
             "your", "yours", "yourself", "yourselves"]

STATES = ["Alabama", "AL", "Nebraska", "NE", "Alaska", "AK", "Nevada", "NV", "Arizona", "AZ", "New Hampshire", "NH", "Arkansas", "AR",
        "New Jersey", "NJ", "California", "CA", "New Mexico", "NM", "Colorado", "CO", "New York", "NY", "Connecticut", "CT",
        "North Carolina", "NC", "Delaware", "DE", "North Dakota", "ND", "District of Columbia", "DC", "Ohio", "OH", "Florida", "FL",
        "Oklahoma", "OK", "Georgia", "GA", "Oregon", "OR", "Hawaii", "HI", "Pennsylvania", "PA", "Idaho", "ID", "Puerto Rico", "PR",
        "Illinois", "IL", "Rhode Island", "RI", "Indiana", "IN", "South Carolina", "SC", "Iowa", "IA", "South Dakota", "SD", "Kansas", "KS",
        "Tennessee", "TN", "Kentucky", "KY", "Texas", "TX", "Louisiana", "LA", "Utah", "UT", "Maine", "ME", "Vermont", "VT", "Maryland", "MD",
        "Virginia", "VA", "Massachusetts", "MA", "Virgin Islands", "VI", "Michigan", "MI", "Washington", "WA", "Minnesota", "MN",
        "West Virginia", "WV", "Mississippi", "MS", "Wisconsin", "WI", "Missouri", "MO", "Wyoming", "WY", "Montana", "MT"]

def remove_punctuation(text):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    if type(text) == float:
        return text
   
    ans = ''
    for i in text:
        if i not in punctuation:
            ans += i
    return ans


def remove_stopwords(text):
    if text.lower() not in STOPWORDS:
        return text
    return ''

def remove_states(text):
    if not any(text in state for state in STATES):
        return text
    return ''


def clean_data(data):
    cleaned_data = []
    for row in data:
        news_words = row.split(' ') 
        removed_stopwords = [remove_stopwords(word) for word in news_words]
        removed_states = [remove_states(word) for word in removed_stopwords]
        clean_words = [remove_punctuation(word) for word in removed_states]
        cleaned_data.append(' '.join(clean_words))

    return cleaned_data