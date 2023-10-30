from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from apps.disk.models.album import Disk


@login_required
def add_disk(request):
    
    if request.method == 'POST':
        # Obter os dados do formulário
        disk_name = request.POST['disk_name']
        genre = request.POST['genre']
        year = request.POST['year']

        # Criar um novo disco
        disk = Disk(
            disk_name=disk_name,
            genre=genre,
            year=year,
        )

        # Salvar o disco no banco de dados
        disk.save()

        # Redirecionar o usuário para a página de listagem
        return redirect('list')

    else:
        return render(request, 'disk/add_disk.html')
