from django.db import models

class Animal(models.Model):
    id_animal = models.BigIntegerField(primary_key=True) #Chave primaria
    numero = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    nascimento = models.DateField()
    pesagens = models.CharField(max_length=10) #Chave Estrangeira


class Pesagem(models.Model):
    id_pesagem = models.BigIntegerField(primary_key=True) #Chave Primaria
    data_pesagem = models.DateField()
    peso = models.FloatField()
