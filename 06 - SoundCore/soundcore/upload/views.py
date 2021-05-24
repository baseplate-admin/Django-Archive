from PIL import Image
from io import BytesIO

from mutagen.flac import FLAC

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from asgiref.sync import async_to_sync, sync_to_async

from upload.forms import FileFieldForm
from upload.models import MusicList


# Create Your Views Here

@login_required()
@sync_to_async()
def file_upload_form(request):
    form = FileFieldForm(request.POST, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for file in files:
                if file.name.endswith('.flac'):
                    flac_dict = FLAC(file)

                    artist = flac_dict.get('artist', None)

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
                    sample_rate = flac_dict.info.sample_rate
                    database_object = MusicList.objects.create(
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
                        mime_type='flac'
                    )
                    database_object.save()
                elif file.name.endswith('mp3'):
                    pass
        return render(request, 'upload/successful/index.html')
    elif request.method == "GET":
        if request.user.is_superuser:
            form = FileFieldForm()

    return render(request, 'upload/index.html', {'form': form})
