from django.urls import path

from .views.cadastrar import cadastrar_aluno
from .views.listar import listar_alunos
from .views.pesquisar import pesquisar_alunos
from .views.visualizar import visualizar_aluno

urlpatterns = [
    path('', listar_alunos, name='listar_alunos'),
    path('cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('visualizar/<int:id>', visualizar_aluno, name='visualizar_aluno'),
    path('editar/<int:id>', editar_aluno, name='editar_aluno'),
    path('excluir/<int:id>', excluir_aluno, name='excluir_aluno'),
]