#from django.core import validators
from django import forms
from .models import User

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobileno', 'nightstay', 'guests', 'intime', 'outtime', 'paymethod']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobileno': forms.TextInput(attrs={'class':'form-control'}),
            'nightstay': forms.NumberInput(attrs={'class':'form-control'}),
            'guests': forms.NumberInput(attrs={'class':'form-control'}),
            'intime': forms.DateTimeInput(attrs={'class':'form-control'}),
            'outtime': forms.DateTimeInput(attrs={'class':'form-control'}),
            'paymethod': forms.TextInput(attrs={'class':'form-control'}),
            # 'photo' : forms.  \
        }
        labels = {'name':'Name', 'email':'Email ID', 'mobileno':'Mobile Number', 'nightstay':'No. of Nights Staying', 'guests':'No. of Guests', 'intime':'Check-in Time','outtime':'Check-out Time','paymethod':'Payment Method'}