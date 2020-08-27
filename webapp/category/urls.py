from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^panel/category/list/$", views.list_category, name="cat_list"),
]
