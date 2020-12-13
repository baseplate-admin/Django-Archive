from . import views
from django.urls import path

urlpatterns = [
    # path("", views.index, name="Redirects to Home"),
    path("polls/<pk>/", views.poll_vote, name="Poll Vote"),
    path("all_poll/", views.all_polls, name="All Polls"),
    path("create_poll/", views.create_poll, name="Create Poll"),
    path("poll_result/<pk>/", views.poll_result, name="Result of a poll"),
    path("thank_you_poll/<pk>/", views.thank_you_poll, name="Thank You"),
]
