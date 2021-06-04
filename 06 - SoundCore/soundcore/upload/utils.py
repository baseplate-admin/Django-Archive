from PIL import Image
from io import BytesIO

from mutagen.flac import FLAC

from django.core.files.base import ContentFile
from django.db import IntegrityError

from upload.models import MusicList
from django.http import Http404


def flac_upload_handler(file):
    """
    This function takes in a flac file extracts info and saves it to database.
    """
    if not file.name.endswith(".flac"):
        raise Http404

    flac_dict = FLAC(file)

    artist = flac_dict.get("artist", None)

    if type(artist) is list:
        artist = artist[0]

    title = flac_dict.get("title", None)

    if type(title) is list:
        title = title[0]

    album = flac_dict.get("album", None)

    if type(album) is list:
        album = album[0]

    date = flac_dict.get("date", None)

    if type(date) is list:
        date = date[0]

    lyricist = flac_dict.get("lyricist", None)

    if type(lyricist) is list:
        lyricist = lyricist[0]

    composer = flac_dict.get("composer", None)

    if type(composer) is list:
        composer = composer[0]

    try:
        picture = flac_dict.pictures[0]
        im = Image.open(BytesIO(picture.data))
        _in_memory_object = BytesIO()
        im.save(_in_memory_object, format="PNG")
        image = ContentFile(_in_memory_object.getvalue(), f"{title}.png")

    except IndexError:
        image = None

    bitrate = flac_dict.info.bitrate
    length = flac_dict.info.length
    sample_rate = flac_dict.info.sample_rate
    try:
        MusicList.objects.create(
            song_name=title,
            song_file=file,
            artist=artist,
            album=album,
            album_art=image,
            date=date,
            lyricist=lyricist,
            composer=composer,
            bitrate=bitrate,
            length=length,
            sample_rate=sample_rate,
            mime_type="flac",
        ).save()
    except IntegrityError:
        # Prevent the save of Same Object Multiple times.
        pass
