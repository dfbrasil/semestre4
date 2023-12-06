
from django.urls import path
from .views import aluno_list, aluno_create, aluno_update, aluno_delete

urlpatterns = [
    path('list/', aluno_list, name='aluno_list'),
    path('create/', aluno_create, name='aluno_create'),
    path('update/<int:id>', aluno_update, name='aluno_udate'),
    path('delete/<int:id>', aluno_delete, name='aluno_delete'),
]
