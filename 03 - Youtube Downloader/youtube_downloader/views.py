from django.shortcuts import render
from django.shortcuts import redirect
import youtube_dl
from .models import Youtube
import os

from datetime import datetime
# Create your views here.

time = None
title = None


def home_redirect(request):
    return redirect("youtube_video/")


def home_youtube_video(request):
    return render(request, "front/home.html")


def download_video(request):
    from datetime import date

    obj_now = datetime.now()
    hour = obj_now.hour
    minute = obj_now.minute
    second = obj_now.second
    microsecond = obj_now.microsecond
    year = obj_now.year
    month = obj_now.month
    date = date.today()
    global time
    time = f"{date}-{month}-{year}--{hour}-{minute}-{second}-{microsecond}"
    mediatimedirexists = os.path.isdir(f"/media/{time}")

    if not bool(mediatimedirexists):
        os.mkdir(f"./media/{time}/")
    
    form = request.POST.get("url_request")

    # page = urllib.request.urlopen(form)
    # html = BeautifulSoup(page.read(), "html.parser")
    # bs4_title = html.title.string

    media_dir = os.path.abspath(os.path.realpath(f"media/{time}/%(title)s.%(ext)s"))

    ydl_options = {
        "format": "bestaudio/best",
        "outtmpl": media_dir,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }],
    }
    global title
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        info_dict = ydl.extract_info(form, download=False)
        ydl.prepare_filename(info_dict)
        title = info_dict['title']
        title = title.replace('/', "_")
        ydl.download([form])

    # download_link = f"media/{time}/{bs4_title}"
    media_file_location = f"/media/{time}/{title}.mp3"
    database = Youtube.objects.create(
        title=title,
        url=form,
        file_location=media_file_location,
        time=time,
    )
    database.save()
    return redirect("/download_create/")


def download_template(request):
    global time
    link = Youtube.objects.get(time=time).file_location
    return render(request, "front/download.html", {
        "link":link
    })


# def media_downloader(request, time_value, title):
#     return redirect(f"/media/{time_value}/{title}.mp3")

# Media download works.
