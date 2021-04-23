from django.db import models

# Create your models here.


class HttpsModel(models.Model):
    binary = models.BigIntegerField()
    completed = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Telementry"

