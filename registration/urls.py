from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('register/', views.register, name='myregisterpage'),
    path('login/', views.login, name='mylogin'),
    path('home/', views.home, name='myhome'),
   path('about_us/', views.home, name='about_us'),
   path('contact_us/', views.home, name='contact_us'),

]
