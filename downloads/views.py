from django.shortcuts import render
from .models import Download


def download(request):
    downloads = Download.objects.all()
    return render(request, 'downloads.html',
    {"downloads": downloads})
