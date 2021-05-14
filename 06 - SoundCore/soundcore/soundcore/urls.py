from django.urls import path
from soundcore import views

urlpatterns = [
    path('home/', views.soundcore_home, name='home'),
    path('library/', views.library_show, name='library_home'),
    path('library/generator/', views.library_generator, name='library_generator')
]
