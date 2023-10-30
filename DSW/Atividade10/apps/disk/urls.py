from django.urls import path

from .views.listview import list_disk
from .views.detailview import detail_disk
from .views.edit_disk import edit_disk
from .views.delete_disk import delete_disk
from .views.readview import read_disk


urlpatterns = [
    path('', list_disk, name='list'),
    path('read/<int:id>', read_disk, name='read'),
    path('edit/<int:id>', edit_disk, name='edit'),
    path('delete/<int:id>', delete_disk, name='delete'),
]
