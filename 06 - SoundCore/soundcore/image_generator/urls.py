from image_generator import views
from django.urls import path

urlpatterns = [
    path('', views.image_gen, name='image_generator')
]
