from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomerRegistration
from .models import User

# Create your views here.
def create_show(request):
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

def retrieve_record(request):    
    cus = User.objects.all()
    return render(request, 'enroll/view_records.html', {'cus':cus})

def delete_record(request, id):
    if request.method == 'POST':
        frm = User.objects.get(pk=id)
        frm.delete()
        return HttpResponseRedirect('/')