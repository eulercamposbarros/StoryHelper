from django.test import TestCase
from composer.models import Historia, Parte, Avalicao

class PartesTest(TestCase):
    def test_incluir_nova_parte(self):
        historia = Historia.objects.create(session='sessao_test')
        historia.incluir_parte(texto='Parte Teste', criado_pelo_usuario=True)
        self.assertTrue(Parte.objects.filter(historia=historia).count() == 1)
    
    def test_obter_ultima_parte_historia(self):
        historia = Historia.objects.create(session='sessao_test')
        historia.incluir_parte(texto='Parte 1', criado_pelo_usuario=True)
        historia.incluir_parte(texto='Parte 2', criado_pelo_usuario=False)
        self.assertTrue(historia.ultima_parte().ordem == 2)

class AvaliacaoTests(TestCase):
    def test_incluir_nova_avaliacao(self):
        historia = Historia.objects.create(session='sessao_test')
        historia.incluir_avaliacao(coerencia=1, diversao=1, comentario='Comentaro teste')
        self.assertTrue(Avalicao.objects.filter(historia=historia).count() == 1)
