from django.shortcuts import render
from django.shortcuts import redirect
import youtube_dl
from .models import Youtube
import os
# from .models import FormYoutube
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

time = None
title = None

# Encryption


class GenerateKey:
    def __init__(self):
        self.key = self.gen_key()

    def gen_key(self):
        from cryptography.fernet import Fernet
        self.key = Fernet.generate_key()
        return self.key

    def does_key_exist(self):
        key_in_db = Youtube.objects.filter(secret=self.key).exists()
        if not key_in_db:
            return self.key
        else:
            self.does_key_exist()


def home_redirect(request):
    return redirect("youtube_video/")


def home_youtube_video(request):
    if request.method == "POST":
        # form_data = FormYoutube(request.POST)
        # if form_data.is_valid():
        form = request.POST.get("url")

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
        # mediatimedirexists = os.path.isdir(f"/media/{time}")
        #
        # if not bool(mediatimedirexists):
        #     os.mkdir(f"./media/{time}/")

        # page = urllib.request.urlopen(form)
        # html = BeautifulSoup(page.read(), "html.parser")
        # bs4_title = html.title.string
        secret = GenerateKey().does_key_exist()
        media_dir = os.path.abspath(
            os.path.realpath(f"media/{time}/%(title)s.%(ext)s")
        )

        ydl_options = {
            "format": "bestaudio/best",
            "outtmpl": media_dir,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
        }
        global title
        with youtube_dl.YoutubeDL(ydl_options) as ydl:
            info_dict = ydl.extract_info(form, download=False)
            ydl.prepare_filename(info_dict)
            title_unchanged = info_dict["title"]
            title = info_dict["title"]

            # Bullshit NTFS Logic
            unsupported_characters = ["<", ">", ":", '"', "/", "\\", "|", "*"]
            for characters in unsupported_characters:
                if characters in title:
                    title = title.replace(characters, "_")

            ydl.download([form])

        # download_link = f"media/{time}/{bs4_title}"
        current_dir = os.getcwd()
        media_file_location = f"{current_dir}/media/{time}/{title}.mp3"

        database = Youtube.objects.create(
            title=title_unchanged,
            url=form,
            file_location=media_file_location,
            time=time,
            secret=secret,
        )
        database.save()
        pk = Youtube.objects.get(secret=secret).pk
        return redirect(f"/download_create/{pk}/")
    else:
        return render(
            request,
            "front/youtube_download_home.html",
        )


# def download_video(request):


def download_template(request, pk):
    secret = Youtube.objects.get(pk=pk).secret.decode("utf-8")
    print(secret)
    return render(
        request,
        "front/youtube_download_download.html",
        {
            "secret": secret,
        },
    )


def download_button(request, secret):
    # global time
    secret = secret.encode("utf-8")

    youtube_download_location = Youtube.objects.get(secret=secret).file_location
    youtube_download_name = f"{Youtube.objects.get(secret=secret).title}.mp3"
    with open(youtube_download_location, 'rb') as file:
        response = HttpResponse(file.read(), content_type='audio/mpeg')
        print(youtube_download_name)
        response['Content-Disposition'] = 'attachment; filename={}'.format(youtube_download_name)
        return response

# TODO
# Media dir creation doesn't work
