from django.shortcuts import render
from apps.control.models.aluno import Aluno

def visualizar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, 'control/visualizar_aluno.html', {
        'aluno': aluno,
    })
