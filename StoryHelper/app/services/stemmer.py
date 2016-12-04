import nltk

stemmer = nltk.stem.RSLPStemmer()

def stem(word):
    return stemmer.stem(word)