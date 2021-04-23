"""
    This api allows images to be hyperlinked. 
    Written in Django
"""

from .models import HttpsModel

from django.db.models import F

from django.views.decorators.cache import cache_page

from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync

# Django imports

from django.http.response import Http404, HttpResponse


# PIL for image resizing

from PIL import Image

from io import BytesIO

# Needed for https_image_resizer

import aiohttp

# Create your views here.


# We dont need get for this api


@sync_to_async
def database(raw_data_length: int) -> None:
    db = HttpsModel.objects.first()

    if not db:
        fake_db = HttpsModel.objects.create(binary=0, completed=0)
        fake_db.save()
        db = HttpsModel.objects.first()

    db.binary = F("binary") + raw_data_length

    db.completed = F("completed") + 1

    db.save()


# We dont need post for this API
@cache_page(60 * 60)
@async_to_sync
async def https_image_resizer_px_based(request):
    """
        Resizes Http Query
        Accepts: 
            Http(Query),
            Size(Query) <-- Not required
            
    """
    if request.method == "GET":
        # Get data from request query param

        http_data = request.GET["url"]

        # Try loop to get size.
        # So if size query param is not defined. It will be none and the raw data will be returned

        try:

            size = request.GET["size"]

        # MultiValueDictError

        except:

            size = None

        # If size is not defined the program will continue

        if size is not None:

            # Converts query params to a tuple

            size_split = size.split("x")

            size_mapped = map(int, size_split)

            size_tupled = tuple(size_mapped)

        # Aiohttp to get data from the http data

        async def request():
            async with aiohttp.ClientSession() as session:

                async with session.get(http_data) as resp:

                    # Reads data from the request url

                    raw_data = await resp.read()

                    # If size is not defined the program will continue

                    if size is not None:

                        # Saves the raw data to memory

                        raw_data_to_memory = BytesIO(raw_data)

                        # Opens the raw data
                        im = Image.open(raw_data_to_memory)

                        # Resizes the raw binary

                        resized = im.resize(size_tupled)

                        # Creates a new in memory object that we can call

                        in_memory = BytesIO()

                        # Saves to memory

                        resized.save(in_memory, format="PNG")

                        # Gets data from memory as binary

                        returnable_value = in_memory.getvalue()

                        # Frees up the memory

                        in_memory.truncate(0)

                        # Sets pos to 0

                        in_memory.seek(0)

                        # Free up the memory

                        raw_data_to_memory.truncate(0)

                        # Sets pos to 0

                        raw_data_to_memory.seek(0)

                        # Finally returns the resized image as binary

                        return returnable_value

                    else:

                        # If no size query is given return the raw data

                        return raw_data

        # Gathers data from result

        result = await request()

        await database(len(result))

        # Return the image with proper Mime Type

        return HttpResponse(result, content_type="image/png")
    else:
        return Http404


@cache_page(60 * 60)
@async_to_sync
async def https_image_resizer_ratio_based(request):
    if request.method == "GET":
        url = request.GET["url"]
        try:
            ratio = request.GET["ratio"]
        except:
            ratio = "16x9"
        try:
            factor = request.GET["factor"]
        except:
            factor = 120

        async def request():
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    raw_data = await response.read()

                    raw_data_to_memory = BytesIO(raw_data)

                    im = Image.open(raw_data_to_memory)

                    list_object = lambda e: e.split("x")

                    map_to_int = lambda e: list(map(int, e))

                    multiply_by_factor = lambda a: a * factor

                    modified_list = list(
                        map(multiply_by_factor, map_to_int(list_object(ratio)))
                    )

                    resized = im.resize(tuple(modified_list))

                    in_memory = BytesIO()

                    resized.save(in_memory, format="PNG")

                    result = lambda e: e.getvalue()

                    return result(in_memory)

        result = await request()
        return HttpResponse(result, content_type="image/PNG")
    else:
        return Http404
