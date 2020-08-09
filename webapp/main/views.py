from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import site_info
from news.models import News
# Create your views here.


def home(request):
    site = site_info.objects.filter(pk=8)
    news = News.objects.all()

    return render(request, 'front/home.html', {
        'site': site,
        "news": news
    })


def about(request):
    site = site_info.objects.filter(pk=8)
    return render(request, 'front/about.html', {
        "site": site
    })


def contact(request):
    site = site_info.objects.filter(pk=8)
    return render(request, "front/contact.html", {
        "site": site
    })


def panel(request):
    site = site_info.objects.filter(pk=8)
    return render(request, "back/home.html", {
        "site": site
    })
