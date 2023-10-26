from django.db import models
from .curso import Curso

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    data_nascimento = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    