from django.shortcuts import render
from django.shortcuts import redirect
from .models import Url
from .models import FormUrl

# Create your views here.
import string
import random


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        short_url = Url.objects.filter(short=rand_letters)
        if not short_url:
            return rand_letters
        else:
            continue


def url_shortener_home(request):
    if request.method == "POST":
        form_data = FormUrl(request.POST)
        if form_data.is_valid():
            form = form_data.cleaned_data["long"]

            database_data = Url.objects.filter(long=form).exists()
            short = shorten_url()

            import datetime

            datetime_object = datetime.datetime.now()

            if database_data:
                url = Url.objects.get(long=form).short
                #       Add redirect to a box.
                return render(
                    request,
                    "front/urlshortener_showaddedurl.html",
                    {
                        "url": url,
                    },
                )

            elif not database_data:
                database = Url.objects.create(
                    long=form, short=short, time=datetime_object
                )
                database.save()
                url = Url.objects.get(long=form).short
                #       Add redirect to a box.
                return render(
                    request,
                    "front/urlshortener_showaddedurl.html",
                    {
                        "url": url,
                    },
                )

            else:
                print("Error")

    elif request.method == "GET":
        form = FormUrl()
        return render(
            request,
            "front/urlshortener_home.html",
            {
                "form": form,
            },
        )


def redirect_to_home(request):
    return redirect("/urlshortener/")


# def create_form(request):
#     if request.method == "GET":
#         return redirect("/home/")


def short_url(request, shorturl):
    database_data = Url.objects.filter(short=shorturl)
    if database_data.exists():
        url = Url.objects.get(short=shorturl).long
        return redirect(url)
    return redirect("/home/")
