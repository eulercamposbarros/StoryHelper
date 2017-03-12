from django.db import models

class Sentence(models.Model):
    sentence = models.TextField()
    next_sentence = models.TextField()
    keys = models.CharField(max_length=1024)
    sujeito =  models.CharField(max_length=1024)