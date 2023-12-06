from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.views.generic.edit import CreateView

def aluno_criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return aluno_listar(request)
    else:
        form = AlunoForm()
            
   
    return render(request, 'aluno/form.html',{'form':form})

def aluno_listar(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos':alunos
    }
    return render(request, 'aluno/aluno_listar.html', context)

def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('aluno_listar')

def aluno_editar(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_listar')
    else:
            form = AlunoForm(instance=aluno)
    return render(request,'aluno/form.html',{'form':form})
