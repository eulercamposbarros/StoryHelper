from django.db import models
from datetime import datetime
   
class Historia(models.Model):
    session = models.CharField(max_length=1024)
    estilo = models.CharField(max_length=1024)

    def incluir_parte(self, texto, criado_pelo_usuario):
        Parte.objects.create(historia=self,texto=texto,criado_pelo_usuario=criado_pelo_usuario,ordem=Parte.objects.filter(historia=self).count()+1)

    def incluir_avaliacao(self, coerencia, diversao, comentario):
        Avalicao.objects.create(historia=self,coerencia=coerencia,diversao=diversao,comentario=comentario)

    def historia_finalizada(self):
        return Avalicao.objects.filter(historia=self).count() > 0

class Parte(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_pelo_usuario = models.BooleanField(default=True)
    ordem = models.IntegerField()

class Avalicao(models.Model):
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)
    coerencia = models.IntegerField()
    diversao = models.IntegerField()
    data = models.DateTimeField(default=datetime.now())
    comentario = models.TextField(null=True)