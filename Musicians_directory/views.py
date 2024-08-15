from django.shortcuts import render, redirect
from .forms import MusicianForm
from .import models,forms
def create_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_musicians')
    else:
        form = MusicianForm()
    return render(request, 'create_musicians.html', {'form': form})



def musician_edit(request, id):
    album = models.Musician.objects.get(pk=id) 
    form = forms.MusicianForm(instance=album)
 
    if request.method == 'POST': 
        form = forms.MusicianForm(request.POST, instance=album) 
        if form.is_valid(): 
            form.save() 
            return redirect('musician_edit') 
    
    return render(request, 'create_musicians.html', {'form' : form})

def musician_delete(request, id):
    post = models.Musician.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')
