from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobileno = models.CharField(max_length=10)
    nightstay = models.IntegerField()
    guests = models.IntegerField()
    intime = models.DateTimeField(default=datetime.now())
    outtime = models.DateTimeField(default=datetime.now())
    amount = models.FloatField(default='0.0')
    paymethod = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="myimage/", default="myimage/AK.jpg")
    



  