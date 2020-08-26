from __future__ import unicode_literals
from django.db import models

# Create your models here.


class News(models.Model):

    name = models.CharField(default=' ', max_length=50)
    card_description = models.TextField(default=' ')
    body_content = models.TextField(default=' ')
    date = models.IntegerField(default="0")
    picurl = models.TextField(default="0")
    picname = models.TextField(default="0")
    writer = models.CharField(default=' ', max_length=20)
    category_name = models.CharField(max_length=50, default='-')
    category_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " | " + str(self.pk)
