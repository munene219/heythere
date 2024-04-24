from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.template import loader #for routing your templates
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from registration.models import student, testmonkey



def registration(request):
    return HttpResponse("Welcome to the registration")

def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def dashboard(request):
    data = testmonkey.objects.all();
    context = {'data': data}
    return render(request, 'dashboard.html', context)

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def contact_us(request):
    template = loader.get_template('contact_us.html')
    return HttpResponse(template.render())

def about_us(request):
    template = loader.get_template('about_us.html')
    return HttpResponse(template.render())

@csrf_exempt
def addstudent(request):
    if request.method == 'POST':
         fname = request.POST.get('firstname')
         lname = request.POST.get('lastname')
         email = request.POST.get('email')
         phone = request.POST.get('phone')
         age = request.POST.get('age')
        # display work in the terminal to see if the code is okay
         mydata = {'firstname': fname, 'lastname': lname, 'email': email, 'phone': phone, 'age': age}
         print(mydata)

         teststudent = testmonkey(firstname=fname, lastname=lname, email=email, phone_number=phone, age=age)
         teststudent.save()

        # fetch the student data to be displayed
        # you rander the request to the place you want the data to be displayed ie:a table in another page
    data = testmonkey.objects.all()
    context = {'data':data}
    return render(request, 'dashboard.html', context)




def editstudent(request,id):
  data = testmonkey.objects.get(id=id)
  context = {'data': data}
  return render(request, 'updatestudent.html', context)

def updatestudent(request,id):
  if request.method == 'POST':
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    age = request.POST.get('age')
    number = request.POST.get('number')

    #modify the student details based on the student id given
    editstudent = testmonkey.objects.get(id=id)
    editstudent.studentname = firstname
    editstudent.studentname = lastname
    editstudent.email = email
    editstudent.age= age
    editstudent.number = number
    editstudent.save()
  return redirect('/dashboard')

def deletestudent(request,id):
  deletestudent = testmonkey.objects.get(id=id)
  deletestudent.delete()
  return redirect('/dashboard')
# Create your views here.

