from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import News
from main.models import site_info
# Create your views here.


def news_details(request, word):
    site = site_info.objects.filter(pk=8)
    news = News.objects.filter(name=zad)

    return render(request, 'front/news_detail.html', {
                'news': news,
                "site": site
    })

    
def news_list(request):
    site = site_info.objects.filter(pk=8)
    return render(request, "back/news_list.html", {
        "site": site
    })
