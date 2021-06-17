from utility import views
from django.urls import path

urlpatterns = [
    path("song", views.get_song, name="song_generator"),
    path("random_song", views.get_random_songs, name="random_song_generator"),
]
