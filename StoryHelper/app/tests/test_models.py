from django.test import TestCase
from app.models import *

class PartesTests(TestCase):
    def test_incluir_nova_parte(self):
        historia = Historia.objects.create(session='sessao_test')
        historia.incluir_parte(texto='Parte Teste', criado_pelo_usuario=True)
        self.assertTrue(Parte.objects.filter(historia=historia).count() == 1)

class AvaliacaoTests(TestCase):
    def test_incluir_nova_avaliacao(self):
        historia = Historia.objects.create(session='sessao_test')
        historia.incluir_avaliacao(coerencia=1, diversao=1, comentario='Comentaro teste')
        self.assertTrue(Avalicao.objects.filter(historia=historia).count() == 1)

