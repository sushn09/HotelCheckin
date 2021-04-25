from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobileno = models.CharField(max_length=10)
    nightstay = models.IntegerField()
    guests = models.IntegerField()
    intime = models.DateTimeField()
    outtime = models.DateTimeField(blank=True)
    paymethod = models.CharField(max_length=10)
    photo = models.ImageField(upload_to="myimage")
    



  