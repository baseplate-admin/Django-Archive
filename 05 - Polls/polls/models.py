from django.db import models
from django import forms

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)
    time = models.CharField(max_length=28)

    def __str__(self):
        return self.question


class IpTable(models.Model):
    entry_id = models.IntegerField()
    ip = models.CharField(max_length=12)


class CreatePollForm(forms.Form):
    question = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "What is your Favourite OS?"}
        ),
    )
    option_1 = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Linux"}),
    )
    option_2 = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Windows"}
        ),
    )
    option_3 = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Mac OS"}
        ),
    )
    option_4 = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "FreeBSD"}
        ),
    )


