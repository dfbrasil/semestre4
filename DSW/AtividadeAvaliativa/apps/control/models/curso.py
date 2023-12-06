from django.db import models


class Curso(models.Model):
    nome = models.CharField(
        verbose_name='Curso:',
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.nome
