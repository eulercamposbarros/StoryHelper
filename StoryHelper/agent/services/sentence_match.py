import StoryHelper, django
django.setup()
from agent.models import Sentence
from agent.tools.tagger import tag
from agent.tools.stemmer import stem
from agent.services.sentence_analyser import get_keys, get_sujeito
import random

def _get_random_sequence(response):
    response['Debug'].append('Não foi encontrado nenhum caso similar. Recuperado um caso aleatorio...')
    opcoes = Sentence.objects.all()
    response['Resposta'] = opcoes[random.choice(range(len(opcoes)))].next_sentence
    response['Debug'].append(response['Resposta'])
    return response

def findsequence(text):
    if Sentence.objects.all().count() == 0:
        raise Exception('O modelo não está treinado')
    
    response = {'Resposta':None,'Debug':[]}
    response['Debug'].append('Taggs: {}'.format(tag(text)))
    keys = get_keys(text)
    response['Debug'].append('Keys: {}'.format(keys))
    stem_key = stem(keys[0])
    opcoes = Sentence.objects.filter(keys__contains=stem_key)
    if len(opcoes) > 0:
        sentence = opcoes[random.choice(range(len(opcoes)))]
        response['Debug'].append('Caso encontrado: {}'.format(sentence.sentence))
        response['Debug'].append('Próximo caso: {}'.format(sentence.next_sentence))
        response['Debug'].append('Tags do próximo caso: {}'.format(tag(sentence.next_sentence)))
        response['Resposta'] = sentence.next_sentence
        sujeito_original = get_sujeito(text)
        sujeito_match = get_sujeito(response['Resposta'])
        if len(sujeito_match) > 0 and len(sujeito_original) > 0:
            response['Debug'].append('Sujeito adaptado: {}'.format(sujeito_match))
            response['Debug'].append('Sujeito original: {}'.format(sujeito_original))
            response['Resposta'] = response['Resposta'].replace(sujeito_match, sujeito_original)
        elif len(sujeito_original) == 0:
            response['Debug'].append('Não foi encontrado sujeito na frase do usuário')
        elif len(sujeito_match) == 0:
            response['Debug'].append('Não foi encontrado sujeito no caso encontrado')
    else:
        return _get_random_sequence(response)        

    return response