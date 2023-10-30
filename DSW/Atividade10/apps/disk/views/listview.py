from django.shortcuts import render

from apps.disk.models.album import Disk


def list_disk(request):
    
    disks = Disk.objects.all()

    return render(request, 'disk/listview.html', {'disks': disks})
