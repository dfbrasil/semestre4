from django.db import models
import pycountry

from .stamp import Stamp


class Disk(models.Model):

    disk_name = models.CharField(
        verbose_name='Nome do disco:',
        max_length=200,
        blank=True,
        null=True,
    )
    
    description = models.CharField(
        verbose_name='Descrição do álbum',
        max_length=200,
        blank=True,
        null=True,
    )
    
    stamp = models.ForeignKey(
        Stamp,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    
    year = models.IntegerField(
        verbose_name='Ano de lançamento',
        blank=True,
        null=True,        
    )
    
    COUNTRY_CHOICES = [
        (country.name, country.name) for country in pycountry.countries
    ]

    country = models.CharField(
        verbose_name='País',
        max_length=100,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True,
        default='Brasil',
    )
    
    GENRE_CHOICES = [
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip_hop', 'Hip-Hop'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('country', 'Country'),
        ('reggae', 'Reggae'),
        ('rap', 'Rap'),
        ('classical', 'Classical'),
        ('electronic', 'Electronic'),
        ('metal', 'Metal'),
        ('folk', 'Folk'),
        ('indie', 'Indie'),
        ('punk', 'Punk'),
        ('soul', 'Soul'),
        ('funk', 'Funk'),
        ('disco', 'Disco'),
        ('r&b', 'R&B'),
        ('techno', 'Techno'),
        ('dance', 'Dance'),
        ('alternative', 'Alternative'),
        ('house', 'House'),
        ('ska', 'Ska'),
        ('blues_rock', 'Blues Rock'),
        ('pop_rock', 'Pop Rock'),
        ('country_rock', 'Country Rock'),
        ('heavy_metal', 'Heavy Metal'),
        ('samba', 'Samba'),
        ('bossa_nova', 'Bossa Nova'),
        ('forro', 'Forró'),
        ('sertanejo', 'Sertanejo'),
        ('pagode', 'Pagode'),
        ('axé', 'Axé'),
        ('mpb', 'Música Popular Brasileira'),
        ('funk_carioca', 'Funk Carioca'),
        ('sertanejo_universitario', 'Sertanejo Universitário'),
        ('brega', 'Brega'),
        ('maracatu', 'Maracatu'),
        ('frevo', 'Frevo'),
        ('coco', 'Coco'),
        ('xote', 'Xote'),
        ('regional', 'Música Regional'),
        ('samba_rock', 'Samba-Rock'),
        ('choro', 'Choro'),
        ('rap_brasileiro', 'Rap Brasileiro'),
        ('tropicalia', 'Tropicália'),
    ]
    
    genre = models.CharField(
        verbose_name='Gênero musical:',
        max_length=150,
        choices=GENRE_CHOICES,
        blank=True,
        null=True,
        default='Rock',
    )
    
    quantity = models.IntegerField(
        verbose_name='Quantidade a ser adquirida:',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.disk_name
        