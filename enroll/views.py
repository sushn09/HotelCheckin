from django.shortcuts import render
from .forms import CustomerRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = CustomerRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = CustomerRegistration()
    else:
        fm = CustomerRegistration()
        # cus = User.objects.all()
    return render(request, 'enroll/add_and_show.html', {'form':fm})