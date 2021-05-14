from .forms import FileFieldForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from asgiref.sync import async_to_sync, sync_to_async

from mutagen.flac import FLAC
from upload.models import MusicList

from PIL import Image
from io import BytesIO

from django.core.files.base import ContentFile


# Create Your Views Here

@login_required()
@async_to_sync
async def file_upload_form(request):
    @sync_to_async()
    def save_music_to_database(_title, _song_file, _artist, _album, _album_art, _date, _lyricist, _composer, _bitrate,
                               _length, _music_extension):
        database_object = MusicList.objects.create(
            song_name=_title,
            song_file=_song_file,
            artist=_artist,
            album=_album,
            album_art=_album_art,
            date=_date,
            lyricist=_lyricist,
            composer=_composer,
            bitrate=_bitrate,
            length=_length,
            music_extension=_music_extension
        )
        database_object.save()

    form = FileFieldForm(request.POST, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for file in files:
                if file.name.endswith('.flac'):
                    flac_dict = FLAC(file)

                    artist = flac_dict.get('composer', None)

                    if type(artist) is list:
                        artist = artist[0]

                    title = flac_dict.get('title', None)

                    if type(title) is list:
                        title = title[0]

                    album = flac_dict.get('album', None)

                    if type(album) is list:
                        album = album[0]

                    date = flac_dict.get('date', None)

                    if type(date) is list:
                        date = date[0]

                    lyricist = flac_dict.get('lyricist', None)

                    if type(lyricist) is list:
                        lyricist = lyricist[0]

                    composer = flac_dict.get('composer', None)

                    if type(composer) is list:
                        composer = composer[0]

                    try:
                        picture = flac_dict.pictures[0]
                        im = Image.open(BytesIO(picture.data))
                        _in_memory_object = BytesIO()
                        im.save(_in_memory_object, format='PNG')
                        image = ContentFile(_in_memory_object.getvalue(), f'{title}.png')

                    except IndexError:
                        image = None

                    bitrate = flac_dict.info.bitrate
                    length = flac_dict.info.length

                    await save_music_to_database(
                        _song_file=file,
                        _title=title,
                        _artist=artist,
                        _bitrate=bitrate,
                        _length=length,
                        _album=album,
                        _date=date,
                        _lyricist=lyricist,
                        _composer=composer,
                        _album_art=image,
                        _music_extension="FLAC"
                    )

                elif file.name.endswith('mp3'):
                    pass
        return render(request, 'upload/successful/index.html')
    elif request.method == "GET":
        if request.user.is_superuser:
            form = FileFieldForm()

    return render(request, 'upload/index.html', {'form': form})
