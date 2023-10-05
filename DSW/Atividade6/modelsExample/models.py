from django.db import models

class Sebo(models.Model):
    
    nome = models.CharField(
        max_length=50,
        blank=True,
    )
    
    descricao = models.TextField(
        max_length=200,
        blank=True,
    )
    
    selo_fonografico = models.CharField(
        max_length=50,
        blank=True,
    )
    
    ano = models.IntegerField(
        blank=True,
    )
    
    pais = models.CharField(
        max_length=200,
        blank=True,
    )
    
    genero = models.CharField(
        max_length=50,
        blank=True,
    )
    
    quantidade = models.IntegerField(
        blank=True,
    )
    
    def __str__(self):
        return self.nome