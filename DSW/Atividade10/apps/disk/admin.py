from django.contrib import admin
from .models.disk import Disk
from .models.artist import Artist
from .models.stamp import Stamp

@admin.register(Disk)
class DiskAdmin(admin.ModelAdmin):
    list_display=[
        'disk_name',
    ]
    
    list_filter = [
        'disk_name',
        'genre',
    ]
    
    search_fields=[
        'genre',
    ]

@admin.register(Stamp)
class StampAdmin(admin.ModelAdmin):
    list_display=[
        'stamp',
    ]
    
    list_filter = [
        'stamp',
    ]
    
    search_fields=[
        'stamp',
    ]
    
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    
    list_filter = [
        'artist_name',
        'albums',
    ]
    
    search_fields=[
        'albums',
    ]
