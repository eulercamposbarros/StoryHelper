import nltk.corpus

stopwords = nltk.corpus.stopwords.words('portuguese')

def clear(sentence):
    return [w for w in sentence if w not in stopwords]