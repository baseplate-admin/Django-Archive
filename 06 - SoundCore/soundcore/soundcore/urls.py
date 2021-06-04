from django.urls import path
from soundcore import views

urlpatterns = [
    path("home.py", views.soundcore_home, name="home"),
    path("library.py", views.library_show, name="library_home"),
    path(
        "libraries/<str:short_url>.py", views.library_items_show, name="library_item_show"
    ),
    path("library/generator.py", views.library_generator, name="library_generator"),
]
