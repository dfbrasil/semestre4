from django.shortcuts import render
from .models import Aluno
from .forms import AlunoForm

def aluno_list(request):
    aluno = Aluno.objects.all()
    return render(request, 'aluno/aluno_list.html', {'aluno':aluno})

def aluno_create(request):
    