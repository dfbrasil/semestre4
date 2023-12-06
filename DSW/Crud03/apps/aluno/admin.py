from django.contrib import admin
from .models import Aluno, Curso, Cidade
# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list = ('nome')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list = ('curso')
    
@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list = ('cidade')