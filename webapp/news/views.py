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
    news = News.objects.all()
    return render(request, "back/news_list.html", {
        "site": site,
        "news": news
    })


def news_add(request):
    site = site_info.objects.filter(pk=8)
    if request.method == "POST":
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        shorttext = request.POST.get('shorttext')
        bodytext = request.POST.get('bodytext')

        if newstitle == "" or newscategory == "" or shorttext == "" or bodytext == "":
            error = "All Fields Required!!!"
            return render(request, "back/error.html", {
                "error": error,
            })

        b = News(name=newstitle, card_description=shorttext, body_content=bodytext, date="2020",pic="-", writer="-", category_name=newscategory, category_id=0, show=0)
        b.save()
        return redirect("news_list")
    return render(request, "back/news_add.html", {
        "site": site,
    })
