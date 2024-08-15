# from django import forms
# from .models import album

# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = album
#         fields = '__all__'

from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
 