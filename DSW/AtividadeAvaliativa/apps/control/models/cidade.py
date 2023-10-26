from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
        