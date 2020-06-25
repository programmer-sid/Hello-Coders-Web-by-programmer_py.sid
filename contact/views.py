from django.shortcuts import render
from django.http import HttpResponse
from.models import Contact

def contact(request):
    return render(request, 'contact.html')

def sent(request):
    if request.method == 'POST':
        emailr = request.POST.get('youremail')
        subr = request.POST.get('yoursubject')
        msgr = request.POST.get('yourmsg')
        
        c = Contact(email=emailr, subject=subr, message=msgr)
        c.save()
    
    return render(request, 'new.html')