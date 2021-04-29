#from django.core import validators
from django import forms
from .models import User

ROOM_TYPE= [
    ('Single Room', 'Single Room'),
    ('Double Room', 'Double Room'),
    ('Triple Room', 'Triple Room'),
    ('Twin Room', 'Twin Room'),
    ('Connecting Room', 'Connecting Room'),
    ('Murphy Room', 'Murphy Room'),
    ]

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobileno', 'guests', 'room', 'nightstay', 'indate', 'intime', 'outdate', 'outtime', 'amount', 'paymethod', 'photo', 'agree']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobileno': forms.TextInput(attrs={'class':'form-control'}),
            'guests': forms.NumberInput(attrs={'class':'form-control'}),
            'room':forms.RadioSelect(choices=ROOM_TYPE),
            'nightstay': forms.NumberInput(attrs={'class':'form-control'}),
            'indate':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'intime': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'outdate':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'outtime': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'amount': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {'name':'Name', 'email':'Email ID', 'mobileno':'Mobile Number', 'guests':'No. of Guests', 'room':'Type of room', 'nightstay':'No. of Nights Staying', 'indate':'Check-in Date', 'intime':'Check-in Time', 'outdate':'Check-out Date', 'outtime':'Check-out Time', 'amount':'Amount', 'paymethod':'Payment Method', 'photo':'Verification'}
