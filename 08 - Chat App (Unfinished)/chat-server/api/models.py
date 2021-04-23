from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Models(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)

    def __str__(self) -> str:
        return str(self.user)
