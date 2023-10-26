from django.shortcuts import render, redirect, get_object_or_404
from apps.control.models.aluno import Aluno

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.nome = request.POST['nome']
        aluno.endereco = request.POST['endereco']
        aluno.email = request.POST['email']
        aluno.data_nascimento = request.POST['data_nascimento']
        aluno.curso_id = request.POST['curso'] 
        aluno.cidade_id = request.POST['cidade'] 

        aluno.save()
        return redirect('listar_alunos')

    context = {
        'aluno': aluno,
    }

    return render(request, 'control/editar_aluno.html', context)
