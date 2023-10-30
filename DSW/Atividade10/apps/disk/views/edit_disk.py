from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.disk.models.album import Disk


def edit_disk(request, id):
    
    disk = Disk.objects.get(id=id)

    if request.method == 'POST':
        disk_name = request.POST['disk_name']
        genre = request.POST['genre']
        year = request.POST['year']

        disk.disk_name = disk_name
        disk.genre = genre
        disk.year = year

        disk.save()

        return redirect('list')

    else:
        return render(request, 'disk/edit_disk.html', {'disk': disk})