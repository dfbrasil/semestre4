from django.shortcuts import render
from apps.disk.models.artist import Artist
from apps.disk.models.album import Disk
from apps.disk.models.stamp import Stamp

def DetailDiskView(request, disk_id):
    
    disk = Disk.objects.get(id=disk_id)

    artists = Artist.objects.filter(albums=disk)

    stamp = disk.stamp
    
    context = {
        'disk': disk,
        'artists': artists,
        'stamp': stamp,
    }
    
    return render(request, 'disk/detailview.html', context)