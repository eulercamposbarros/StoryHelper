from nltk import download_shell
import StoryHelper, django
django.setup()
from app.models import *
from app.services.tagger import tag
from app.services.stemmer import stem
from app.services.formatter import format_tokenarray
import random

def configure_nltk():
    download_shell()

def get_keys(text):
    tagged_phrase = tag(text)
    keys = [x[0] for x in tagged_phrase if x[1].startswith('V')]
    if not keys: keys = [x[0] for x in tagged_phrase if x[1]=='NOUN']
    if not keys: keys = [x[0] for x in tagged_phrase if x[1]=='N']
    if not keys: keys = [tagged_phrase[0][0]]
    return keys

def get_sujeito(text):
    tagged_phrase = tag(text)
    sujeitos = [x[0] for x in tagged_phrase if x[1]=='NPROP']
    if len(sujeitos) > 0:
        nomes_compostos = ''
        pos_nprop = 0
        for i in range(len(tagged_phrase)):
            if tagged_phrase[i][1]=='NPROP':
                pos_nprop = i
                nomes_compostos = tagged_phrase[i][0]
                break
        for i in range(len(tagged_phrase)):
            if i > pos_nprop:
                if tagged_phrase[i][1]=='NPROP' or tagged_phrase[i][1]=='NOUN':
                    nomes_compostos += ' ' + tagged_phrase[i][0]
                else:
                    break
        if len(nomes_compostos) > 0: return nomes_compostos
        if len(sujeitos) > 1: return sujeitos[0]
        return format_tokenarray(sujeitos)
    return ''

def get_contexto(text):
    pass

def match(text):
    tagged = tag(text)
    print('Taggs - {}'.format(tagged))
    keys = get_keys(tagged)
    print('Keys - {}'.format(keys))
    stem_key = stem(keys[0])
    # nelhorar o macth das keys
    sentence = Sentence.objects.filter(keys__contains=stem_key).first()
    if sentence != None:
        print('Sentence - {}'.format(sentence.sentence))
        print('Next Sentence - {}'.format(sentence.next_sentence))
        sujeito_original = get_sujeito(text)
        resposta = sentence.next_sentence
        sujeito_match = get_sujeito(resposta)
        if len(sujeito_match) > 0:
            print('Sujeito Match - {}'.format(sujeito_match))
            print('Sujeito Original - {}'.format(sujeito_original))
            resposta = resposta.replace(sujeito_match, sujeito_original)
        return resposta
    else:
        opcoes = Sentence.objects.all()
        return opcoes[random.choice(range(len(opcoes)))].next_sentence
