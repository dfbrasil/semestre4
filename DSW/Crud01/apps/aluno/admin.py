from django.contrib import admin

from .models import Aluno, Cidade, Curso

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display=('nome_aluno','endereco','email')

@admin.register(Cidade)
class EnderecoAdmin(admin.ModelAdmin):
    list=('cidade')
    
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list=('curso')
