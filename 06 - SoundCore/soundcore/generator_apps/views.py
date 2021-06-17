import io

from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from asgiref.sync import async_to_sync, sync_to_async

from upload.models import MusicList


# Create your views here.


@login_required()
@async_to_sync
async def get_song(request):
    @sync_to_async()
    def database(__id: int):
        __data = MusicList.objects.get(id=__id)
        return __data

    async def _get_path(_id: int):
        _database = await database(__id=_id)
        __data = _database.song_file
        _media_path = settings.MEDIA_ROOT
        _file_location = f"{_media_path}/{__data}"

        return _file_location

    if request.method == "GET":

        __id = request.GET["id"]
        __database = await database(__id)
        _mime_type = __database.mime_type

        _data = await _get_path(_id=__id)

        if _mime_type == "flac":
            if not settings.DEBUG:
                response = HttpResponse()
                response['X-Sendfile'] = _data
                del response['content-type']
                return response
            else:
                with open(_data, 'rb') as f:
                    data = io.BytesIO(f.read())
                    return HttpResponse(data, content_type='audio/flac')
        else:
            raise Http404
    else:
        raise Http404
