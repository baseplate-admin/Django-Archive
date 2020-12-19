from django.urls import path
from . import views

urlpatterns = [
    path("urlshortener/", views.url_shortener_home, name="Home"),
    path("", views.redirect_to_home, name="Redirects to home"),
    # path("create_form/", views.create_form, name="Creates a Form"),
    path("urlshortener/<shorturl>/", views.short_url, name="Short Urls"),
]
