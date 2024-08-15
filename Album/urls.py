from django.urls import path
from . import views
urlpatterns = [
    
    path('new/',views.create_album,name='create_album'),
    path('edit/<int:id>/', views.album_edit, name='album_edit'),
    path('delete/<int:id>/', views.album_delete, name='album_delete'),
  
]