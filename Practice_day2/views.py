from django.shortcuts import render
from Album.models import Album
from Musicians_directory.models import Musician 

def home(request):
    musicians = Musician.objects.all()  
    albums = Album.objects.all()  
    context = {
        'musicians': musicians,
        'albums': albums
    }
    return render(request, 'home.html', context)  

