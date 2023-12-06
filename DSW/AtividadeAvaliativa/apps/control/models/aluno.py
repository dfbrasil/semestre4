from django.db import models
from .curso import Curso
from .cidade import Cidade

class Aluno(models.Model):
    nome = models.CharField(
        verbose_name='Nome:',
        max_length=255,
        blank=True,
        null=True,
    )
    endereco = models.CharField(
        verbose_name='Endereço:',
        max_length=255,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Email:',
        blank=True,
        null=True,
    )
    data_nascimento = models.DateField(
        verbose_name='Data de nascimento:',
        blank=True,
        null=True,
    )
    curso = models.ForeignKey(
        Curso, 
        on_delete=models.CASCADE
    )
    cidade = models.ForeignKey(
        Cidade, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome
    