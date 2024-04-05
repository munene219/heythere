from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registerpage/', views.mypage, name='myregisterpage'),
    path('login/', views.login, name='mylogin'),
    path('home/', views.home, name='myhome')
]