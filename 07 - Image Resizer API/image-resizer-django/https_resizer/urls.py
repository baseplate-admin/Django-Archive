from https_resizer import views
from django.urls import path

urlpatterns = [
    path("api/v1/image_resize/https/px/", views.https_image_resizer_px_based),
    path("api/v1/image_resize/https/ratio/", views.https_image_resizer_ratio_based),
]
