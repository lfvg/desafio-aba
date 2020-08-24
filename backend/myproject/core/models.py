from django.db import models

# Create your models here.


class Departamento(models.Model):
    nome = models.CharField(max_length=20)

class User(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    funcao = models.CharField(max_length=50)
    idade = models.IntegerField()