from django.urls import path

from .views import aluno_listar, aluno_criar, aluno_editar, aluno_remover

    
urlpatterns = [
    path('', aluno_listar, name='aluno_listar'),
    path('aluno/', aluno_criar, name='aluno_criar'),
    path('aluno/remover/<int:id>', aluno_remover, name='aluno_remover'),
    path('aluno/editar/<int:id>', aluno_editar, name='aluno_editar'),
]