import email

from django.db import models

class SigninForm(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)


# Create your models here.
class SignupForm(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)
