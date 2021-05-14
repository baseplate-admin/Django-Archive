from django.shortcuts import render
from upload.models import MusicList
from django.http import Http404
from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.decorators import login_required

from soundcore.forms import LibraryGeneratorForm
from soundcore.models import LibraryGenerator


# Create your views here.

async def soundcore_home(request):
    @sync_to_async()
    def get_music_from_db():
        return MusicList.objects.all()

    @sync_to_async()
    def render_template(_dict):
        return render(request, 'soundcore/index.html', _dict)

    if request.method == "GET":
        musics = await get_music_from_db()
        __request = await render_template({'musics': musics})
        return __request

    elif request.method == "POST":
        raise Http404


@login_required()
@async_to_sync
async def library_show(request):
    @sync_to_async()
    def get_all_library():
        return LibraryGenerator.objects.all()

    if request.method == "GET":
        data = await get_all_library()
        return render(request, 'soundcore/library/index.html', {'libraries': data})
    elif request.method == "POST":
        raise Http404


@login_required()
def library_generator(request):
    if request.method == "POST":
        form = LibraryGeneratorForm(request.POST)
        if form.is_valid():
            pass

    elif request.method == "GET":
        form = LibraryGeneratorForm()
        return render(request, 'soundcore/library/create/index.html', {'form': form})
