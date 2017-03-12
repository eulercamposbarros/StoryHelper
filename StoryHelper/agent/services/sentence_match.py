import StoryHelper, django
django.setup()
from agent.models import Sentence
from agent.tools.tagger import tag
from agent.tools.stemmer import stem
from agent.services.sentence_analyser import get_keys, get_sujeito
import random

def findsequence(text):
    if Sentence.objects.all().count() == 0:
        raise Exception('O modelo não está treinado')

    print('Taggs - {}'.format(tag(text)))
    keys = get_keys(text)
    print('Keys - {}'.format(keys))
    stem_key = stem(keys[0])
    # TODO: nelhorar o macth das keys
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