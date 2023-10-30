from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.disk.models.album import Disk

def delete_disk(request, id):
    
    disk = Disk.objects.get(id=id)

    # Excluir o disco do banco de dados
    disk.delete()

    # Redirecionar o usuário para a página de listagem
    return redirect('list')