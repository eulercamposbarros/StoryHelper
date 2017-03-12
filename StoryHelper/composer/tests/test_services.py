from django.test import TestCase
from composer.models import *
from composer.services import services

class SujeitoTests(TestCase):
    def test_get_sujeito_simples(self):
        frase = 'O leitor superficial conclui daqui que o nosso Mendonça era um homem excêntrico.'
        sujeito = services.get_sujeito(frase)
        self.assertTrue(sujeito == 'Mendonça')

    def test_get_sujeito_duplo(self):
        frase = 'Era conveniente ao romance que o leitor ficasse muito tempo sem saber quem era Miss Dollar.'
        sujeito = services.get_sujeito(frase)
        self.assertTrue(sujeito == 'Miss Dollar')

    def test_get_sujeito_multiplo(self):
        frase = 'Quase se pode dizer que, no espírito de Mendonça, o cão pesava tanto como o amor, segundo uma expressão célebre: tirai do mundo o cão, e o mundo será um ermo.'
        sujeito = services.get_sujeito(frase)
        self.assertTrue(sujeito == 'Mendonça', sujeito)

    def test_get_sujeito_multiplo(self):
        frase = 'Naquele tempo ainda o Barão do Amazonas não tinha salvo a independência das repúblicas platinas mediante a vitória de Riachuelo, nome com que depois a Câmara Municipal crismou a Rua de Mata-cavalos.'
        sujeito = services.get_sujeito(frase)
        self.assertTrue(sujeito == 'Barão do Amazonas', sujeito)

