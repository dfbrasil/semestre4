from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request,'aluno/aluno_list.html',{'alunos':alunos})

def aluno_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
        form = AlunoForm()
    
    return render(request, 'aluno/aluno_form.html', {'form':form})

def aluno_update(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('aluno_list')
    else:
            form = AlunoForm(instance=aluno)
            
    return render(request,'aluno/aluno_form.html',{'form':form})

def aluno_delete(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    
    return render(request, 'aluno/aluno_delete_confirm.html', {'aluno':aluno})