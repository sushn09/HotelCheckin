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
    



  