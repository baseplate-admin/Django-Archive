from generator_apps import views
from django.urls import path

urlpatterns = [
    path("song.py", views.get_song, name="song_generator"),
    path("image/full.py", views.full_image_gen, name="full_image_generator"),
    path('image/resized.py', views.resized_image_gen, name="resized_image_generator"),
]
