from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path("index/", views.all_songs, name="hydrates_the_songs")]
