import io

from asgiref.sync import async_to_sync, sync_to_async
from django.http import Http404
from django.http import HttpResponse
from upload.models import MusicList
from django.conf import settings
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60 * 60)
@async_to_sync
async def image_gen(request):
    @sync_to_async()
    def get_image(_id: int):
        __image = MusicList.objects.get(id=_id).album_art
        media_path = settings.MEDIA_ROOT
        file_location = f'{media_path}/{__image}'
        return file_location

    @sync_to_async()
    def get_binary_from_image(path: str):
        with open(path, 'rb') as f:
            _in_memory = io.BytesIO(f.read())
        return _in_memory.getvalue()

    if request.method == "GET":
        image_id = request.GET.get("id", None)
        if not image_id:
            raise Http404
        image = await get_image(image_id)
        binary = await get_binary_from_image(image)
        return HttpResponse(binary, content_type='image/png')

    elif request.method == 'POST':
        raise Http404
