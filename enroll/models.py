from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobileno = models.CharField(max_length=10)
    guests = models.IntegerField()    
    room = models.CharField(max_length=100, null=True)
    nightstay = models.IntegerField()
    indate = models.DateField(null=True)
    intime = models.TimeField(null=True)
    outdate = models.DateField(null=True)
    outtime = models.TimeField(null=True)
    amount = models.FloatField(default=0.0)
    
    PAYMENT_OPTIONS= [
        ('--Select--', '--Select--'),
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('PhonePay', 'PhonePay'),
        ('Net Banking', 'Net Banking'),
        ('UPI ID', 'UPI ID'),
        ('Paytm', 'Paytm'),
        ]
    paymethod = models.CharField(max_length=100, choices=PAYMENT_OPTIONS, default="--Select--", )
    photo = models.ImageField(upload_to="myimage/", default="myimage/AK.jpg")
    agree = models.BooleanField("I agree to the T&C", default=False, blank=False)
    



  