from django.db import models
from upload.models import MusicList
from django.contrib.auth.models import User


# Create your models here.


class UserVolumeInputCapture(models.Model):
    volume = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} | {self.volume}"


class UserPreviousSongCapture(models.Model):
    previous_song = models.ForeignKey(MusicList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user} | {self.previous_song}"

    def save(self, *args, **kwargs):
        # Allow 1/4 th Saving.
        if UserPreviousSongCapture.objects.count() >= (MusicList.objects.count() / 4):
            UserPreviousSongCapture.objects.first().delete()
        super().save(*args, **kwargs)
