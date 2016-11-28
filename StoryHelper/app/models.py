"""
Definition of models.
"""

from django.db import models
from datetime import datetime

class Sentence(models.Model):
    sentence = models.TextField()
    next_sentence = models.TextField()

class Writer(models.Model):
    email = models.EmailField(null=True)
    nome = models.CharField(max_length=1024, null=True)
    data = models.DateTimeField(default=datetime.now())
    comentario = models.TextField(null=True)
    
class Historia(models.Model):
    titulo = models.CharField(max_length=1024)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    def incluir_parte(self, texto):
        Parte.objects.create(historia=self,texto=texto,ordem=Parte.objects.filter(historia=self).count()+1)

class Parte(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    texto = models.TextField()
    ordem = models.IntegerField()