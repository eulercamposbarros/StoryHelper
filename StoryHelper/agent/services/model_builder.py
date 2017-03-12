import StoryHelper, django
django.setup()
from agent.models import Sentence
from agent.tools.tagger import tag
from agent.tools.formatter import format_tokenarray
from nltk.corpus import machado
from agent.tools.time_measure import measure
from agent.services.sentence_analyser import get_keys, get_sujeito
from queue import Queue

sents = machado.sents()[:10000]
total_sents = len(sents)

def _persist_sentence(q):
    data = []
    while not q.empty():
        print(q.qsize())
        sent_data = q.get()
        sent_text = format_sentence(format_tokenarray(sent_data[0]))
        nextsent_text = format_sentence(format_tokenarray(sent_data[1]))
        if not is_valid_sentence(sent_text) or not is_valid_sentence(nextsent_text): continue
        if len(get_sujeito(sent_text)) == 0 or len(get_keys(sent_text)) == 0: continue
        tagged = tag(sent_text)
        if not all([x[0]==x[1] for x in tagged]):
            data.append(Sentence(sentence=sent_text,
                                    next_sentence=nextsent_text,
                                    keys=format_tokenarray(get_keys(sent_text),';').lower(),
                                    sujeito=get_sujeito(sent_text)))
    print('Persisting...')
    Sentence.objects.bulk_create(data,batch_size=len(data))

def is_valid_sentence(sent):
    if sent == sent.upper(): return False
    if sent.strip()[-1:] == ':': return False
    if sent.strip()[-1:] == ',': return False
    return True

def format_sentence(sent):
    return sent.strip()

@measure
def build_model(clear_data=False):
    if clear_data:
        [s.delete() for s in Sentence.objects.all()]
    q = Queue()
    [q.put((sents[i], sents[i+1])) for i in range(0, total_sents - 1)]
    _persist_sentence(q)
