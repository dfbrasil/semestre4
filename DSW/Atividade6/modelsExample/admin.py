from django.contrib import admin

from .models import Sebo, SeloFonografico, Artista

admin.site.register(Sebo)
# admin.site.register(Choice)
admin.site.register(SeloFonografico)
admin.site.register(Artista)
