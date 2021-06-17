from soundcore import views
from django.urls import path

urlpatterns = [
    path("home/", views.soundcore_home, name="home"),
    path("library/", views.library_show, name="library_home"),
    path(
        "libraries/<str:short_url>/", views.library_items_show, name="library_item_show"
    ),
    path(
        "library/generator/",
        views.library_generator,
        name="library_generator",
    ),
]
