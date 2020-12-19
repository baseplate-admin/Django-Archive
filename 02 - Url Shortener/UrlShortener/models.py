from __future__ import unicode_literals
from django.db import models
from django import forms

# Create your models here.


class Url(models.Model):
    long = models.CharField(unique=True, max_length=1000)
    short = models.CharField(unique=True, max_length=25)
    time = models.CharField(default="-", max_length=2000)

    def __str(self):
        return self.long


# class FormUrl(forms.Form):
#     long = forms.URLField(label="Enter Url:")
    # widget = forms.TextInput(attrs={'class': "btn btn-dark"})
