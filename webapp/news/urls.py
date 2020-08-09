from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^news/(?P<zad>.*)/$", views.news_details, name="news_details"),
    url(r"^panel/news/list/$", views.news_list, name="news_list")
]
