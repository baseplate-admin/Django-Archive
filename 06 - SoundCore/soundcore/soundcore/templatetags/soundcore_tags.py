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


@register.filter(name="to_two_decimal")
def to_two_decimal(number):
    return round(float(number), 2)
