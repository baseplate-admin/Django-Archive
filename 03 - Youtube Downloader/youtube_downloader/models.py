from django.db import models

# Create your models here.


class Youtube(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    file_location = models.TextField()
    time = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.title
