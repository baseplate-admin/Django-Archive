from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import News
from main.models import site_info
from django.core.files.storage import FileSystemStorage
import datetime
# Create your views here.


def news_details(request, zad):
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

    date_time = datetime.datetime.now()

    year = date_time.year
    month = date_time.month
    day = date_time.day

    day_string = str(day)
    month_string = str(month)
    year_string = str(year)

    if len(day_string) == 1:
        day = "0" + day_string
    if len(month_string) == 1:
        month = "0" + month_string
    if len(year_string) == 1:
        year = "0" + year_string

    if (request.method == "POST"):
        newstitle = request.POST.get('newstitle')
        newscategory = request.POST.get('newscategory')
        shorttext = request.POST.get('shorttext')
        bodytext = request.POST.get('bodytext')

        if (newstitle == ""
                or
                newscategory == ""
                or
                shorttext == ""
                or
                bodytext == ""):
            error = "All Fields Required!!!"
            return render(request, "back/error.html", {
                "error": error,
            })
        try:
            up_file = request.FILES['uploaded_file']
            fs = FileSystemStorage()
            fname = fs.save(up_file.name, up_file)
            fname_url = fs.url(fname)
            if (str(up_file.content_type).startswith("image")):
                if (up_file.size < 5000000):
                    zad = News(name=newstitle,
                               card_description=shorttext,
                               body_content=bodytext,
                               date="2020",
                               picname=fname,
                               picurl=fname_url,
                               writer="-",
                               category_name=newscategory,
                               category_id=0,
                               show=0)
                    zad.save()
                    return redirect("news_list")
                else:
                    error = "Your file must be under 5MB."
                    return render(request, "back/error.html", {
                        "error": error,
                    })
            else:
                error = "Your uploaded File is not an Image."
                return render(request, "back/error.html", {
                    "error": error,
                })
        except Exception:
            error = "Please Upload Images"
            return render(request, "back/error.html", {
                "error": error,
            })

    return render(request, "back/news_add.html", {
        "site": site,
    })
