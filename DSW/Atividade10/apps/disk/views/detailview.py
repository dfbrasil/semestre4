from django.shortcuts import render
from apps.disk.models.artist import Artist
from apps.disk.models.album import Disk
from apps.disk.models.stamp import Stamp

def detail_disk(request, disk_id):
    
    disk = Disk.objects.get(id=disk_id)

    artists = Artist.objects.filter(artist_name=disk)

    stamp = Stamp.objects.filter(stamp=disk)
    
    context = {
        'disk': disk,
        'artists': artists,
        'stamp': stamp,
    }
    
    return render(request, 'disk/detailview.html', context)