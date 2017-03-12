from agent.tools.tagger import tag
from agent.tools.formatter import format_tokenarray

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