from email import message
from sre_constants import SUCCESS
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import is_valid_path
from django.views.generic.edit import FormView
from requests import request
from django.contrib import messages

from pages.models import Contact
# Create your views here.
def home(request):
    return render(request,'pages/base.html')

def ContactView(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        mail=request.POST.get('mail')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact.name=name
        contact.mail=mail
        contact.subject=subject
        contact.message=message
        contact.save()
        messages.success(request,'Mesajiniz iletildi')
    return render(request,'pages/contact.html')    





            
