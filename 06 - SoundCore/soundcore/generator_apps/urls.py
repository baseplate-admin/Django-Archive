from generator_apps import views
from django.urls import path

urlpatterns = [
    path('image/', views.image_gen, name='image_generator'),
    path('song/', views.get_song, name='song_generator')

]
