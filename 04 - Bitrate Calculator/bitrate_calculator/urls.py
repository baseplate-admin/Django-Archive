from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_redirection, name="Redirects to home"),
    path("bitrate/", views.bitrate, name="Shows the Homepage"),
]
