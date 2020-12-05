from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Url(models.Model):
    long = models.CharField(unique=True, max_length=1000)
    short = models.CharField(unique=True, max_length=25)

    def __str(self):
        return self.long
