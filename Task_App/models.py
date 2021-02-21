from django.db import models
from .validators import Namevalidator, PasswordValidator, MobileNoValidator

# Create your models here.

class Manager(models.Model):
    email       = models.EmailField(unique=True)
    firstName   = models.CharField(max_length=100, validators=[Namevalidator])
    lastName    = models.CharField(max_length=100, validators=[Namevalidator])
    password    = models.CharField(max_length=20, validators=[PasswordValidator])
    address     = models.CharField(max_length=500)
    dob         = models.DateField()
    company     = models.CharField(max_length=100)


class Employee(models.Model):
    email       = models.EmailField(unique=True)
    firstName   = models.CharField(max_length=100, validators=[Namevalidator])
    lastName    = models.CharField(max_length=100, validators=[Namevalidator])
    password    = models.CharField(max_length=20, validators=[PasswordValidator])
    address     = models.CharField(max_length=500)
    dob         = models.DateField()
    company     = models.CharField(max_length=100)
    mobile      = models.CharField(max_length=10, validators=[MobileNoValidator])
    city        = models.CharField(max_length=100)