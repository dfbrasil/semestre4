from django.db import models

class SeloFonografico(models.Model):
    
    selo_fonografico = models.CharField(
        max_length=50,
        verbose_name='Noma da Gravadora',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.selo_fonografico
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
    
    selo = models.ForeignKey(
        SeloFonografico,
        on_delete=models.CASCADE,
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
    
class Artista(models.Model):
    
    nome = models.CharField(
        verbose_name="nome do artista",
        max_length=50,
        blank=True,
        null=True,
    )
    
    disco = models.ManyToManyField(
        Sebo,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.nome
    
    
# class Choice(models.Model):
#     choice_text = models.CharField(
#         max_length= 200,
#         verbose_name= " Qual o numero de votos",
#         blank= True,
#     )
#     votes = models.IntegerField(
#         verbose_name="Número de votos",
#         blank=True,
#     )
#     question = models.ForeignKey(
#         Sebo,
#         verbose_name="Questão",
#         on_delete=models.CASCADE,
#         )
    
#     def __str__ (self):
#         return self.choice_text
    
#     O selo fonográfico deve deixar de ser apenas um atributo de texto do disco e passar a ser uma classe. Um disco deve ter apenas um selo fonográfico e um selo fonográfico poderá estar em vários discos;
# Crie um modelo Artista. O modelo artista poderá possuir vários discos e um disco poderá ser gravado por vários artistas.