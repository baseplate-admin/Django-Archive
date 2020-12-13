from django.db import models
from django import forms

# Create your models here.


class Bitrate(models.Model):
    hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()
    size = models.DecimalField(decimal_places=2, max_digits=6)
    episode = models.CharField(default="-", max_length=20)
    time = models.CharField(max_length=200, unique=True, default="-")
    bitrate = models.CharField(max_length=2000, default="--")

    def __str__(self):
        return self.id


# class ModelBitrate(forms.Form):
#     hour = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     minute = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     second = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     size = forms.DecimalField(
#         decimal_places=2, widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     episode = forms.IntegerField(
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
