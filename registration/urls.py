from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='myhome'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='myhome'),

]
