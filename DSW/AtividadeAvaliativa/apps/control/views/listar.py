from django.shortcuts import render
from apps.control.models.aluno import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar_alunos.html', {
        'alunos': alunos,
    })
