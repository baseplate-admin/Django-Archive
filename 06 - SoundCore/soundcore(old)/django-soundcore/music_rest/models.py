from __future__ import unicode_literals
from django.db import models

# Create your models here.


class SoundCoreModel(models.Model):
    author = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    album_art = models.CharField(max_length=200, default="-")
    music_file = models.CharField(max_length=200, default="-")
    release_date = models.CharField(max_length=10, default="-")

    def __str__(self):
        return self.title
