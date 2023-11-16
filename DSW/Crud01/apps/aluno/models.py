from django.db import models

class Cidade(models.Model):
    
    cidade = models.CharField(
        verbose_name='Cidade:',
        max_length=100,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.cidade
    
class Curso(models.Model):
    
    CHOICES_CURSOS = [
        ('Apicultura', 'Apicultura'),
        ('ADS', 'ADS'),
        ('Alimentos', 'Alimentos'),
        ('Quimica', 'Química'),
    ]
    
    curso = models.CharField(
        verbose_name='Curso:',
        choices=CHOICES_CURSOS,
        max_length=100,
        blank=True,
        null=True    
    )
    
    def __str__(self) -> str:
        return self.curso
    
class Aluno(models.Model):
    
    nome_aluno = models.CharField(
        verbose_name='Nome do Aluno',
        max_length=250,
        blank=True,
        null=True
    )
    
    email = models.EmailField(
        verbose_name='Email:',
        max_length=250,
        blank=True,
        null=True
    )
    
    idade = models.IntegerField(
        verbose_name='Idade:',
        blank=True,
        null=True
    )
    
    cidade = models.ForeignKey(
        Cidade,
        verbose_name='Endereço do aluno',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    endereco = models.CharField(
        verbose_name='Endereco do Aluno',
        max_length=250,
        blank=True,
        null=True,
    )
    
    curso = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    def __str__(self) -> str:
        return self.nome_aluno
