from django.test import TestCase
from composer.models import *
from composer.services import model_builder

class SujeitoTests(TestCase):
    def test_build_model(self):
        model_builder.build_model()
        self.assertTrue(Sentence.objects.count() > 0)

    def test_build_model_with_clear(self):
        [s.delete() for s in Sentence.objects.all()]
        model_builder.build_model()
        total = Sentence.objects.all().count()
        [s.delete() for s in Sentence.objects.all()]
        model_builder.build_model(True)
        self.assertTrue(Sentence.objects.count() == total)

    def test_valid_sentence_maisculo(self):
        sentence = 'MISS DOLLAR'
        self.assertFalse(model_builder.is_valid_sentence(sentence))

    def test_valid_sentence_terminado_acento(self):
        sentence = 'Texto-fonte :'
        self.assertFalse(model_builder.is_valid_sentence(sentence))