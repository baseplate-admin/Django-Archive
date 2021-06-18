import io
import json
from django.http import Http404
from django.conf import settings
from django.core import serializers
from upload.models import MusicList
from soundcore.models import LibraryGenerator
from utility.models import UserVolumeInputCapture
from utility.models import UserPreviousSongCapture
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required()
def get_song(request):
    if request.method == "GET":
        _id = request.GET["id"]
        database = MusicList.objects.get(id=_id)

        mime_type = database.mime_type
        data = database.song_file
        media_path = settings.MEDIA_ROOT
        file_location = f"{media_path}/{data}"

        if mime_type == "flac":
            if not settings.DEBUG:
                response = HttpResponse()
                response["X-Sendfile"] = file_location
                del response["content-type"]
                return response
            else:
                with open(file_location, "rb") as f:
                    data = io.BytesIO(f.read())
                    return HttpResponse(data, content_type="audio/flac")
        else:
            raise Http404


@csrf_protect
def get_random_songs(request):
    if request.method == "POST":
        # This will be powered by an AI.
        database = MusicList.objects.order_by("?").first()
        data = serializers.serialize("json", [database])
        return JsonResponse(data, safe=False)


@csrf_protect
def get_four_random_images(request, pk):
    if request.method == "POST":
        database = (
            LibraryGenerator.objects.get(id=pk)
            .prefetch_related("musics")
            .order_by("?")[:4]
        )
        data = serializers.serialize("json", [database])
        return JsonResponse(data, safe=False)


@login_required()
@csrf_protect
def user_volume_capture(request):
    """
    A Simple way to store User Volume
    """
    if request.method == "GET":
        database = UserVolumeInputCapture.objects.filter(user=request.user)
        if not database.exists():
            # If the user visits the site for first time set volume to 50
            UserVolumeInputCapture.objects.create(user=request.user, volume=50).save()
            database = UserVolumeInputCapture.objects.filter(user=request.user)

        data = serializers.serialize("json", database, fields=("volume",))

        return JsonResponse(data, safe=False)
    elif request.method == "POST":
        data_dictionary = dict(request.POST.lists())
        for volume in data_dictionary:
            try:
                database = UserVolumeInputCapture.objects.get(user=request.user)
            except ObjectDoesNotExist:
                data = UserVolumeInputCapture.objects.create(
                    user=request.user, volume=50
                )
                data.save()
                database = UserVolumeInputCapture.objects.get(user=request.user)
            database.volume = volume
            database.save()
        return HttpResponse(status=200)


@login_required()
@csrf_protect
def user_previous_song_capture(request):
    if request.method == "GET":
        database = UserPreviousSongCapture.objects.filter(user=request.user).last()
        data = serializers.serialize("json", [database], fields=("previous_song",))
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        request_data = request.POST
        for item in request_data:
            data = json.loads(item)["pk"]
            if not (UserPreviousSongCapture.objects.last().previous_song.id == data):
                UserPreviousSongCapture.objects.create(
                    previous_song=MusicList.objects.get(id=data), user=request.user
                ).save()
            return HttpResponse(status=200)
