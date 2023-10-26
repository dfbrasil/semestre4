from django.shortcuts import render, redirect
from django.forms import ModelForm
from apps.control.models.aluno import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'endereco', 'email', 'data_nascimento', 'curso', 'cidade']

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'control/cadastrar_aluno.html', {
        'form': form,
    })
