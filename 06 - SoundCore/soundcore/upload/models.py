from django.db import models


# Create your models here.


class MusicList(models.Model):
    song_name = models.CharField(max_length=1024, default='', unique=True)
    song_file = models.FileField(upload_to='songs/')
    artist = models.CharField(max_length=1024, default='', null=True)
    album = models.CharField(max_length=1024, default='', null=True)
    album_art = models.FileField(upload_to='album_arts/')
    date = models.CharField(max_length=1024, default='', null=True)
    composer = models.CharField(max_length=1024, default='', null=True)
    lyricist = models.CharField(max_length=1024, default='', null=True)
    bitrate = models.IntegerField(default=0, null=True)
    length = models.CharField(default='', max_length=10, null=True)
    music_extension = models.CharField(default='', max_length=5)

    def __str__(self) -> str:
        return str(self.id)
