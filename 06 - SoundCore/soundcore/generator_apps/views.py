import io

from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from asgiref.sync import async_to_sync, sync_to_async

from upload.models import MusicList


# Create your views here.


@async_to_sync
async def get_song(request):
    @sync_to_async()
    def database(__id: int):
        __data = MusicList.objects.get(id=__id)
        return __data

    async def _get_data(_id: int, _database):
        __data = __database.song_file
        _media_path = settings.MEDIA_ROOT
        _file_location = f"{_media_path}/{__data}"

        try:
            with open(_file_location, "rb") as f:
                __binary_data = io.BytesIO(f.read())

        except ObjectDoesNotExist:
            raise Http404

        return __binary_data.getvalue()

    if request.method == "GET":
        __id = request.GET["id"]
        __database = await database(__id)
        _mime_type = __database.mime_type

        _data = io.BytesIO(await _get_data(_id=__id, _database=__database)).getvalue()

        if _mime_type == "flac":
            return HttpResponse(_data, content_type="audio/flac")
        else:
            raise Http404
    else:
        raise Http404
