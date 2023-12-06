from django.urls import path
from .views import aluno_list, aluno_create

urlpatterns = [
    path('list/', aluno_list, name='aluno_list'),
    path('create/', aluno_create, name='aluno_create')
]