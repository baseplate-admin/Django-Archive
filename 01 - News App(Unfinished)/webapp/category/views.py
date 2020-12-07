from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import zad_cat
from main.models import site_info


# Create Your model here.


def list_category(request):
    zad_site = site_info.objects.filter(pk=8)
    cat_cat = zad_cat.objects.all()
    return render(
        request,
        "back/list_category.html",
        {
            "cat_cat": cat_cat,
            "site": zad_site,
        },
    )
