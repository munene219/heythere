from django.db import models

class student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(blank=True, null=True, max_length=100)
# Create your models here.python

class testmonkey(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone_number = models.IntegerField(blank=True, null=True)

