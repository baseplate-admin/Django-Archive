from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):

    name = models.CharField(default=' ', max_length=50)
    card_description = models.TextField(default=' ')
    body_content = models.TextField(default=' ')
    date = models.DateTimeField()
    pic = models.TextField()
    writer = models.CharField(default=' ', max_length=20)

    def __str__(self):
        return self.name + " | " + str(self.pk)
