from __future__ import unicode_literals

from django.db import models

class Casal(models.Model):
    nome= models.CharField(max_length=150,unique=True)
    data_evento = models.DateField()

    def __unicode__(self):
        return self.nome

class Presente(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.FloatField()

    def __unicode__(self):
        return self.nome

class Desejos(models.Model):
    casal = models.ForeignKey(Casal)
    desejo = models.ManyToManyField(Presente)


    def __unicode__(self):
        return self.desejo.__str__()