from django.urls import path

from .views.listview import DiskListView
from .views.detailview import DetailDiskView

urlpatterns = [
    path('list/', DiskListView, name='list'),
    path('detail/<int:disk_id>', DetailDiskView, name='detail'),
]