from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader #for routing your templates

from registration.models import student


def registration(request):
    return HttpResponse("Welcome to the registration")

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())

def about_us(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())


def addstudent(request):
    if request.method == 'POST':
     fname = request.POST.get('fname')
     lname = request.POST.get('lname')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     age = request.POST.get('age')
     query=student(firstname=fname,lastname=lname,email=email,phone=phone,age=age)
     query.save()
        # fetch the student data to be displayed
    data = student.objects.all()
    context = {'data':data}
    return render(request, 'register.html', context)
# Create your views here.

