import nltk.data

sent_detector = nltk.data.load('tokenizers/punkt/portuguese.pickle')

def tokenize_sentences(text):
    return [x for x in sent_detector.tokenize(text.strip())]

def tokenize_words(text):
    return [x for x in nltk.tokenize.word_tokenize(text, 'portuguese')]