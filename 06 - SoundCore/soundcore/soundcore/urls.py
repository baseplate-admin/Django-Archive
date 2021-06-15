from django.urls import path
from soundcore import views

urlpatterns = [
    path("home/", views.soundcore_home, name="home"),
    path("soundcore_library/", views.library_show, name="library_home"),
    path(
        "libraries/<str:short_url>/", views.library_items_show, name="library_item_show"
    ),
    path("soundcore_library/generator/", views.library_generator, name="library_generator"),
]
