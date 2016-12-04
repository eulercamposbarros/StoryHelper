import StoryHelper, django
django.setup()
from app.models import *
from app.services import tagger, services
from app.services.formatter import format_tokenarray
from nltk.corpus import machado
from multiprocessing import Process, Queue, cpu_count, Pool
from app.services.tools.time_measure import measure
from app.services.services import get_keys, get_sujeito

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
        if len(get_sujeito(sent_text)) == 0 and len(get_keys(sent_text)) == 0: continue
        tagged = tagger.tag(sent_text)
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

@measure
def build_model_multiprocessed():
    q = Queue()
    [q.put((sents[i], sents[i+1])) for i in range(0, total_sents - 1)]
    procs = [Process(target=_persist_sentence, args=(q,)) for _ in range(cpu_count())]
    [p.start() for p in procs]
    [p.join() for p in procs]
