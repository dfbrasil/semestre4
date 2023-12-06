from django.shortcuts import render
from django.db.models import Q
from apps.control.models.aluno import Aluno

def pesquisar_alunos(request):
    pesquisa = request.GET.get('pesquisa', '')
    alunos = Aluno.objects.filter(
        Q(nome__icontains=pesquisa) |
        Q(endereco__icontains=pesquisa) |
        Q(email__icontains=pesquisa) |
        Q(curso__icontains=pesquisa) |
        Q(cidade__icontains=pesquisa)
    )
    return render(request, 'control/pesquisar_alunos.html', {
        'alunos': alunos,
        'pesquisa': pesquisa,
    })
