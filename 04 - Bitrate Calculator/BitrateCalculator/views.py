from django.shortcuts import render
from django.shortcuts import redirect
from .models import Bitrate


# Calculator class


class _Bitrate:
    def __init__(self):
        self.minute = 0
        self.hour = 0
        self.size = 0
        self.episodes = 0
        self.seconds = 0
        self.bitrate = 0

    def hour_to_seconds(self):
        self.seconds += self.hour * 3600
        return self.seconds

    def minute_to_seconds(self):
        self.seconds += self.minute * 60
        return self.seconds

    def calculate(self):
        filesize = (self.size / self.episodes) * (1024 * 1024) * 8
        time = self.seconds
        self.bitrate = filesize / time
        return self.bitrate

    def input(self, minute, hour, size, episodes, seconds):
        self.minute = minute
        self.hour = hour
        self.size = size
        self.episodes = episodes
        self.seconds = seconds
        self.hour_to_seconds()
        self.minute_to_seconds()
        self.calculate()
        return self.bitrate

        # return self.minute, self.hour, self.size, self.episodes, self.seconds


# Create your views here.


def home_redirection(request):
    return redirect("/bitrate/")


def bitrate(request):
    if request.method == "POST":
        # minute = form.cleaned_data["minute"]
        # hour = form.cleaned_data["hour"]
        # seconds = form.cleaned_data["second"]
        # size = form.cleaned_data["size"]
        # episodes = form.cleaned_data["episode"]
        # print(size)
        # print(minute)
        # print(hour)
        # print(seconds)
        # Time Gen Function
        hour = int(request.POST.get("hour"))
        minute = int(request.POST.get("minute"))
        seconds = int(request.POST.get("seconds"))
        size = float(request.POST.get("size"))
        episodes = int(request.POST.get('count'))

        import datetime

        datetime_object = datetime.datetime.now()

        __bitrate = _Bitrate().input(minute, hour, size, episodes, seconds)

        database = Bitrate.objects.create(
            minute=minute,
            hour=hour,
            second=seconds,
            size=size,
            episode=episodes,
            time=datetime_object,
            bitrate=__bitrate,
        )
        database.save()
        return render(
            request,
            "front/bitrate_result.html",
            {
                "result": __bitrate,
            },
        )


    return render(
        request,
        "front/bitrate_calculator_home.html",
    )


