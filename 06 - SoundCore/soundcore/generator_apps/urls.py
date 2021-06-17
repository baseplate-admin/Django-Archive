from generator_apps import views
from django.urls import path

urlpatterns = [
    path("song", views.get_song, name="song_generator"),
]
