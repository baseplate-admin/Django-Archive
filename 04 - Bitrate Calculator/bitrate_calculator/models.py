from django.db import models


# Create your models here.


class Bitrate(models.Model):
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()
    size = models.DecimalField(decimal_places=2, max_digits=6)
    episode = models.CharField(default='-', max_length=20)
    time = models.CharField(max_length=200, unique=True,default='-')
    bitrate = models.CharField(max_length=2000,default='--')

    def __str__(self):
        return self.id
