from django.db import models
from upload.models import MusicList
from django.contrib.auth.models import User


# Create your models here.

class LibraryGenerator(models.Model):
    musics = models.ManyToManyField(MusicList)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)
