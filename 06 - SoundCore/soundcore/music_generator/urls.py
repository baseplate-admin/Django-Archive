from django.urls import path
from music_generator import views

urlpatterns = [
    path('', views.get_song, name='song_generator')
]
