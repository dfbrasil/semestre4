from django.shortcuts import render, redirect, get_object_or_404
from apps.control.models.aluno import Aluno

def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')

    context = {
        'aluno': aluno,
    }

    return render(request, 'control/excluir_aluno.html', context)
