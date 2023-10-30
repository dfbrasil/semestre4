from django.urls import path

from .views.listview import list_disk
from .views.detailview import detail_disk
from .views.readview import read_disk

urlpatterns = [
    path('', list_disk, name='list'),
    path('read/<int:id>', read_disk, name='read'),
    path('detail/<int:disk_id>', detail_disk, name='detail'),
]