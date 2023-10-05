from django.db import models

class Sebo(models.Model):
    
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome do Artista',
        blank=True,
        null=True,
    )
    
    descricao = models.TextField(
        max_length=200,
        verbose_name='Descrição do Álbum',
        blank=True,
        null=True,
    )
    
    selo_fonografico = models.CharField(
        max_length=50,
        verbose_name='Noma da Gravadora',
        blank=True,
        null=True,
    )
    
    ano = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Ano de lançamento',        
    )
    
    pais = models.CharField(
        max_length=200,
        verbose_name='País de lançamento',
        blank=True,
        null=True,
    )
    
    genero = models.CharField(
        verbose_name='Gênero musical',
        max_length=50,
        blank=True,
        null=True,
    )
    
    quantidade = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Número de cópias',
    )
    
    def __str__(self):
        return self.nome