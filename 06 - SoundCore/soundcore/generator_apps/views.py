import io
from PIL import Image

from django.http import Http404
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from asgiref.sync import async_to_sync, sync_to_async

from upload.models import MusicList


# Reusable Functions


@sync_to_async()
def get_image(_id: int):
    _image = MusicList.objects.get(id=_id).album_art
    media_path = settings.MEDIA_ROOT
    file_location = f"{media_path}/{_image}"
    return file_location


async def get_binary_from_image(path: str):
    with open(path, "rb") as f:
        _in_memory = io.BytesIO(f.read())
        f.close()
        return _in_memory.getvalue()


# Create your views here.


@login_required()
@async_to_sync
async def full_image_gen(request):
    if request.method == "GET":
        image_id = request.GET.get("id", None)
        if not image_id:
            raise Http404
        image = await get_image(image_id)
        binary = await get_binary_from_image(image)
        return HttpResponse(binary, content_type="image/png")

    elif request.method == "POST":
        raise Http404


@login_required()
@async_to_sync
async def resized_image_gen(request):
    # Lambda Functions
    async def list_object(e):
        return e.split("x")

    async def map_to_int(e):
        return list(map(int, e))

    def multiply_by_factor(a):
        return a * factor

    async def result_function(e):
        return e.getvalue()

    if request.method == "GET":

        _id = request.GET.get("id", None)
        ratio = request.GET.get("ratio", "16x9")
        factor_str = request.GET.get("factor", "120")

        factor = int(factor_str)
        if not _id:
            raise Http404

        image_path = await get_image(_id=_id)
        raw_data = await get_binary_from_image(image_path)

        raw_data_to_memory = io.BytesIO(raw_data)

        im = Image.open(raw_data_to_memory)

        modified_list = list(
            map(multiply_by_factor, await map_to_int(await list_object(ratio)))
        )

        resized = im.resize(tuple(modified_list))

        in_memory = io.BytesIO()

        resized.save(in_memory, format="PNG")

        result = await result_function(in_memory)

        return HttpResponse(result, content_type="image/PNG")
    else:
        raise Http404


@login_required()
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
