from django.shortcuts import render
from apps.control.models.aluno import Aluno

def pesquisar_alunos(request, pesquisa):
    alunos = Aluno.objects.filter(
        Q(nome__icontains=pesquisa) |
        Q(idade__icontains=pesquisa) |
        Q(email__icontains=pesquisa) |
        Q(cidade__icontains=pesquisa) |
        Q(curso__icontains=pesquisa)
    )
    return render(request, 'alunos/pesquisar_alunos.html', {
        'alunos': alunos,
        'pesquisa': pesquisa,
    })
