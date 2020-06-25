from django.shortcuts import render
from yourblog.models import YourBlog


def index(request):
    userblog = YourBlog.objects.all()
    return render(request,'usersection.html', 
    {'ub': userblog})
