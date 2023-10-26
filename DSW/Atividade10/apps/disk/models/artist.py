from django.db import models
from django.apps import apps
from .disk import Disk


class Artist(models.Model):
    
    artist_name = models.CharField(
        verbose_name='Nome do Artista',
        max_length=100,
        blank=True,
        null=True,
    )
    
    albums = models.ManyToManyField(
        Disk,
        blank=True,
    )
    
    def __str__(self):
        return self.artist_name or ""
