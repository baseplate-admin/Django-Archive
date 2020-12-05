from django.shortcuts import render
from django.shortcuts import redirect
from .models import Url

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
            shorten_url()

def url_shortener_home(request):

    return render(
        request,
        "front/home.html",
    )


def redirect_to_home(request):
    return redirect("/home/")


def create_form(request):
    if request.method=="POST":
        form = request.POST.get("url_request")
        database_data = Url.objects.filter(long=form).exists()
        short = shorten_url()
        if database_data:
            url = Url.objects.get(long=form).short
            #       Add redirect to a box.
            return render(request, "front/addurl.html", {
                "url": url,
            })
        elif not database_data:
            database = Url.objects.create(long=form, short=short)
            database.save()
            url = Url.objects.get(long=form).short
            #       Add redirect to a box.
            return render(request, "front/addurl.html", {
                "url": url,
            })
        else:
            print("Error")
        return redirect("/home/")
    elif request.method == "GET":
        return redirect("/home/")


def short_url(request, shorturl):
    database_data = Url.objects.filter(short=shorturl)
    if database_data.exists():
        url = Url.objects.get(short=shorturl).long
        return redirect(url)
    return redirect("/home/")