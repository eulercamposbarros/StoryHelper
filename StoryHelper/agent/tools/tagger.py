import nltk
from agent.tools import object_io
from datetime import datetime
from pathlib import Path

tagger_path = 'venv/tagger.pkl'
tagger = None

def _simplify_tag(t):
    if "+" in t:
        return t[t.index("+")+1:]
    else:
        return t

def _build_tagger():
    global tagger
    file = Path(tagger_path)

    if tagger != None: return

    if file.is_file():
        tagger = object_io.read_object(tagger_path)
    else:
        print('{} - Building train data...'.format(datetime.now()))

        dataset = nltk.corpus.floresta.tagged_sents() + \
                  nltk.corpus.mac_morpho.tagged_sents()
        traindata = [[( w , _simplify_tag(t)) for (w , t) in sent] for sent in dataset]

        print('{} - Training POS tagging model...'.format(datetime.now()))

        tagger = nltk.NgramTagger(4, traindata,
                        backoff=nltk.TrigramTagger(traindata,
                        backoff=nltk.BigramTagger(traindata,
                        backoff=nltk.UnigramTagger(traindata,
                        backoff=nltk.DefaultTagger('NOUN')))))

        print('{} - Saving tagger object...'.format(datetime.now()))

        object_io.save_object(tagger, tagger_path)

def tag(text):
    _build_tagger()

    return tagger.tag(nltk.tokenize.word_tokenize(text))
