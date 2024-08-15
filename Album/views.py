from django.shortcuts import render, redirect
from .forms import AlbumForm
from . import models,forms

def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_album')
    else:
        form = AlbumForm()
    return render(request, 'create_album.html', {'form': form})

def album_edit(request, id):
    album = models.Album.objects.get(pk=id) 
    form = forms.AlbumForm(instance=album)
 
    if request.method == 'POST': 
        form = forms.AlbumForm(request.POST, instance=album) 
        if form.is_valid(): 
            form.save() 
            return redirect('album_edit') 
    
    return render(request, 'create_album.html', {'form' : form})

def album_delete(request, id):
    post = models.Album.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
