from django.db import models
import datetime
from Musicians_directory.models import Musician
# Create your models here.
class Album(models.Model):
    #id = models.IntegerField(primary_key=True,unique=True)
    musician =models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name=models.CharField(max_length=50)
    release_date = models.DateField(default=datetime.date.today)
    rating =models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.album_name