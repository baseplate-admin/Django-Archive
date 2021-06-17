import time

from django import template
from soundcore.models import LibraryGenerator

register = template.Library()


@register.inclusion_tag("tags/soundcore_playlist.html", takes_context=True)
def get_total_playlist(context):
    """
    This file is linked to "soundcore/templates/tags/soundcore_playlist.html"
    """
    request = context["request"]
    # Check if user is Authenticated or return No Playlist.
    try:
        playlist = LibraryGenerator.objects.filter(owner=request.user)
    except TypeError:
        playlist = None

    return {"data": playlist, "request": request}


@register.filter(name='format_seconds')
def convert(seconds):
    ty_res = time.gmtime(seconds)
    if 3600 <= seconds:
        res = time.strftime("%H:%M:%S", ty_res)
    elif 3600 > seconds >= 60:
        res = time.strftime("%M:%S", ty_res)
    elif 60 > seconds >= 0:
        res = time.strftime("%Ss", ty_res)
    else:
        res = 0
    return res
