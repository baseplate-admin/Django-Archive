from django.shortcuts import render
from django.shortcuts import redirect
from .models import Url
# from .models import FormUrl

# Create your views here.
import string
import random


# def shorten_url():
#     letters = string.ascii_lowercase + string.ascii_uppercase
#     while True:
#         rand_letters = random.choices(letters, k=5)
#         rand_letters = "".join(rand_letters)
#         short_url = Url.objects.filter(short=rand_letters)
#         if not short_url:
#             return rand_letters
#         else:
#             continue

class ShortUrl:
    def __init__(self):
        self.short_letter = self._short_letter()

    def _short_letter(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        self.short_letter = rand_letters
        return self.short_letter

    def _does_short_exists(self):
        is_true_or_false = Url.objects.filter(short=self.short_letter).exists()
        if is_true_or_false:
            return True
        elif not is_true_or_false:
            return False

    def logic(self):
        if not self._does_short_exists():
            return self.short_letter
        elif self._does_short_exists():
            self._short_letter()




def url_shortener_home(request):
    if request.method == "POST":
        # form_data = FormUrl(request.POST)
        # if form_data.is_valid():
        form = request.POST.get("long")

        database_data = Url.objects.filter(long=form).exists()
        short = ShortUrl().logic()

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
        return render(
            request,
            "front/urlshortener_home.html",
        )


def redirect_to_home(request):
    return render(request, "front/base.html")


# def create_form(request):
#     if request.method == "GET":
#         return redirect("/home/")


def short_url(request, shorturl):
    database_data = Url.objects.filter(short=shorturl)
    if database_data.exists():
        url = Url.objects.get(short=shorturl).long
        return redirect(url)
    return redirect("/home/")
