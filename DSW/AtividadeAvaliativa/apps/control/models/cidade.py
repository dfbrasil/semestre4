from django.db import models

class Cidade(models.Model):
    nome = models.CharField(
        verbose_name='Cidade:',
        max_length=255,
        blank=True,
        null=True,
    )
    sigla_estado = models.CharField(
        verbose_name='UF:',
        max_length=2,
        blank=True,
        null=True,)

    def __str__(self):
        return self.nome
        