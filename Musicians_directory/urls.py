from django.urls import path
from . import views
urlpatterns = [
    
   path('new/',views.create_musician,name='create_musicians'),
   path('edit/<int:id>/', views.musician_edit, name='musician_edit'),
  

   
]