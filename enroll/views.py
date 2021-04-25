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
            mob = fm.cleaned_data['mobile no']
            stay = fm.cleaned_data['nightstay']
            gs = fm.cleaned_data['guests']
            intm = fm.cleaned_data['intime']
            outtm = fm.cleaned_data['outtime']
            pay = fm.cleaned_data['paymethod']
            reg = User(name=nm, email=em, mobileno=mob, nightstay=stay, guests=gs, intime=intm, paymethod=pay)
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

def update_record(request, id):
    if request.method == 'POST':
        fr = User.objects.get(pk=id)
        fm = CustomerRegistration(request.POST, instance=fr)
        if fm.is_valid():
            fm.save()
    else:
        fr = User.objects.get(pk=id)
        fm = CustomerRegistration(instance=fr)
    return render(request, 'enroll/update_customer.html', {'form':fm})


