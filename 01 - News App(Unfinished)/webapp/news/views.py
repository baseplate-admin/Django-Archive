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

    return render(request, "front/news_detail.html", {"news": news, "site": site})


def news_list(request):
    site = site_info.objects.filter(pk=8)
    news = News.objects.all()
    return render(request, "back/news_list.html", {"site": site, "news": news})


def news_add(request):
    zad_site = site_info.objects.filter(pk=8)
    zad_time = datetime.datetime.now()

    year = zad_time.year
    month = zad_time.month
    day = zad_time.day

    day_string = str(day)
    month_string = str(month)

    if len(day_string) == 1:
        day = "0" + day_string
    if len(month_string) == 1:
        month = "0" + month_string

    zad_day = str(year) + "/" + str(month) + "/" + str(day)
    zad_time_form = str(zad_time.hour) + ":" + str(zad_time.minute)

    if request.method == "POST":
        newstitle = request.POST.get("newstitle")
        newscategory = request.POST.get("newscategory")
        shorttext = request.POST.get("shorttext")
        bodytext = request.POST.get("bodytext")

        if newstitle == "" or newscategory == "" or shorttext == "" or bodytext == "":
            error = "All Fields Required!!!"
            return render(
                request,
                "back/error.html",
                {
                    "error": error,
                },
            )

        try:
            up_file = request.FILES["uploaded_file"]
            fs = FileSystemStorage()
            fname = fs.save(up_file.name, up_file)
            fname_url = fs.url(fname)
            if str(up_file.content_type).startswith("image"):
                if up_file.size < 5000000:
                    zad = News(
                        name=newstitle,
                        card_description=shorttext,
                        body_content=bodytext,
                        date=zad_day,
                        time=zad_time_form,
                        picname=fname,
                        picurl=fname_url,
                        writer="-",
                        category_name=newscategory,
                        category_id=0,
                        show=0,
                    )
                    zad.save()
                    return redirect("news_list")
                else:
                    zad_pic = FileSystemStorage()
                    zad_pic.delete(fname)
                    error = "Your file must be under 5MB."
                    return render(
                        request,
                        "back/error.html",
                        {
                            "error": error,
                        },
                    )
            else:
                zad_pic = FileSystemStorage()
                zad_pic.delete(fname)
                error = "Your uploaded File is not an Image."
                return render(
                    request,
                    "back/error.html",
                    {
                        "error": error,
                    },
                )
        except Exception:
            error = "Please Upload Images"
            return render(
                request,
                "back/error.html",
                {
                    "error": error,
                },
            )

    return render(
        request,
        "back/news_add.html",
        {
            "site": zad_site,
        },
    )


def news_delete(request, pk):

    try:
        zad_news = News.objects.get(pk=pk)
        zad_news.delete()

        zad_pic = FileSystemStorage()
        zad_pic.delete(zad_news.picname)

        return redirect(news_list)

    except Exception:
        error = "Something Wrong with Deleting Picture"
        return render(
            request,
            "back/error.html",
            {
                "error": error,
            },
        )
