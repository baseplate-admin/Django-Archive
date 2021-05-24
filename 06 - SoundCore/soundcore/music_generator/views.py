from io import BytesIO

from asgiref.sync import async_to_sync, sync_to_async

from django.views.decorators.cache import cache_page
from django.http import Http404, HttpResponse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from upload.models import MusicList


# Create your views here.

@cache_page(60 * 60)
@async_to_sync
async def get_song(request):
    @sync_to_async()
    def _get_binary(path: str):
        with open(path, 'rb') as f:
            return f.read()

    @sync_to_async()
    def check_mime(_id: int):
        return MusicList.objects.get(id=_id).mime_type

    @sync_to_async()
    def database(__id: int):
        __data = MusicList.objects.get(id=__id).song_file
        return __data

    async def _get_data(_id: int):
        __data = await database(_id)
        _media_path = settings.MEDIA_ROOT
        _file_location = f'{_media_path}/{__data}'

        try:
            __binary_data = BytesIO(await _get_binary(_file_location))
        except ObjectDoesNotExist:
            raise Http404

        return __binary_data.getvalue()

    if request.method == "GET":
        __id = request.GET['id']
        _data = BytesIO(await _get_data(_id=__id)).getvalue()
        _mime_type = await check_mime(__id)

        if _mime_type == 'flac':
            return HttpResponse(_data, content_type='audio/flac')
        else:
            raise Http404

    else:
        raise Http404
