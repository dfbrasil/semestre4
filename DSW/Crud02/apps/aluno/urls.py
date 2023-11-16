from django.urls import path
from .views import AlunoList, AlunoDetail, AlunoCreate,AlunoUpdate, AlunoDelete

urlpatterns = [
    path('aluno_list',AlunoList.as_view(),name='aluno_list'),
    path('aluno_detail/<int:pk>/',AlunoDetail.as_view(), name='aluno_detail'),
    path('aluno_create', AlunoCreate.as_view(), name='aluno_create'),
    path('aluno_update/<int:pk>/', AlunoUpdate.as_view(), name='aluno_update'),
    path('aluno_delete/<int:pk>/', AlunoDelete.as_view(), name='aluno_delete'),
]