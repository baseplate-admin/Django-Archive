from __future__ import unicode_literals
from django.db import models

# Create your models here.


class site_info(models.Model):

    site_name = models.TextField()
    name = models.CharField(default=" ", max_length=15)
    about = models.TextField(default=" ")
    facebook = models.CharField(default=" ", max_length=50)
    github = models.CharField(default=" ", max_length=50)
    youtube = models.CharField(default=" ", max_length=50)
    twitter = models.CharField(default=" ", max_length=50)
    number = models.CharField(default=" ", max_length=18)
    link = models.CharField(default=" ", max_length=50)
    site_creator = models.CharField(default=" ", max_length=15)
    copyright = models.CharField(default=" ", max_length=4)

    def __str__(self):
        return self.site_name + " | " + str(self.pk)
