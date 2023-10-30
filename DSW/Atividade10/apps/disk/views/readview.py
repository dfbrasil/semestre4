from django.shortcuts import render

from apps.disk.models.album import Disk


def read_disk(request,id):
    
    disks = [Disk.objects.get(id=id)]
    
    return render(request, 'disk/readview.html', {'disks': disks})