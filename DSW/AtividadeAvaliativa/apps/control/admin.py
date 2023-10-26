from django.contrib import admin
from .models.cidade import Cidade
from .models.aluno import Aluno
from .models.curso import Curso

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display=[
        'nome',
    ]
    
    list_filter = [
        'nome',
        
    ]
    
    search_fields=[
        'nome',
    ]

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=[
        'nome',
    ]
    
    list_filter = [
        'nome',
    ]
    
    search_fields=[
        'nome',
    ]
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    
    list_filter = [
        'nome',
    ]
    
    search_fields=[
        'nome',
    ]
