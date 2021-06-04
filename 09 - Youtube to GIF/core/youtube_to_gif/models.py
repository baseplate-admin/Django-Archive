from django.db import models


# Create your models here.


class Cache(models.Model):
    cache_key = models.TextField(primary_key=True, unique=True)
    value = models.TextField()
    expires = models.TextField()

    def __str__(self) -> str:
        return str(self.expires)

    class Meta:
        db_table = "django_cache"
