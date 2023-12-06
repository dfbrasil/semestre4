from django.db import models


class Stamp(models.Model):
    stamp = models.CharField(
        verbose_name='Selo Fonográfico',
        max_length=50,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.stamp