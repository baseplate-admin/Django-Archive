from django.urls import path
from . import views

urlpatterns =[
    path('api/v1/youtube/gif/',views.youtube_to_gif)
]