from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home_redirect, name="Redirects to home"),
    path(
        "youtube_video/", views.home_youtube_video, name="Youtube mp3 video Downloader"
    ),
    # path("download/", views.download_video, name="Youtube Download"),
    path("download_create/", views.download_template, name="Youtube Download"),
    # path("download_media/<time>/<bs4_title>", views.media_downloader, name="Manual Video Downloader"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
