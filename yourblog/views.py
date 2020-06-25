from django.shortcuts import render
from.models import YourBlog
from django.http import HttpResponseRedirect

def yourblog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.POST.get('img')
        des = request.POST.get('blog')
        YourBlog(name=name, image_url=img, des=des ).save()
        return HttpResponseRedirect('http://127.0.0.1:8000/userlog')
    return render(request,'yourblog.html')