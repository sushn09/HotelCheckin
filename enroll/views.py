from django.shortcuts import render, HttpResponseRedirect
from .forms import CustomerRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView
from django.views import View

# Create your views here.
class create_show(TemplateView):
    template_name = 'enroll/add_and_show.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = CustomerRegistration()
        cus = User.objects.all()   
        context = {'cus':cus,'form':fm} 
        return context
    
    def post(self, request):
        fm = CustomerRegistration(request.POST, request.FILES)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mob = fm.cleaned_data['mobileno']
            gs = fm.cleaned_data['guests']
            rm = fm.cleaned_data['room']
            stay = fm.cleaned_data['nightstay']
            indt = fm.cleaned_data['indate']
            intm = fm.cleaned_data['intime']
            outdt = fm.cleaned_data['outdate']
            outtm = fm.cleaned_data['outtime']
            amt = fm.cleaned_data['amount']
            pay = fm.cleaned_data['paymethod']
            pic = fm.cleaned_data['photo']
            agree = fm.cleaned_data['agree']
            reg = User(name=nm, email=em, mobileno=mob, guests=gs, room=rm, nightstay=stay, indate=indt, intime=intm, outdate=outdt, outtime=outtm, amount=amt, paymethod=pay, photo=pic, agree=agree)
            reg.save()
            return HttpResponseRedirect('/')

def create_shows(request):
    if request.method == 'POST':
        fm = CustomerRegistration(request.POST, request.FILES)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mob = fm.cleaned_data['mobileno']
            gs = fm.cleaned_data['guests']
            rm = fm.cleaned_data['room']
            stay = fm.cleaned_data['nightstay']
            indt = fm.cleaned_data['indate']
            intm = fm.cleaned_data['intime']
            outdt = fm.cleaned_data['outdate']
            outtm = fm.cleaned_data['outtime']
            amt = fm.cleaned_data['amount']
            pay = fm.cleaned_data['paymethod']
            pic = fm.cleaned_data['photo']
            agree = fm.cleaned_data['agree']
            reg = User(name=nm, email=em, mobileno=mob, guests=gs, room=rm, nightstay=stay, indate=indt, intime=intm, outdate=outdt, outtime=outtm, amount=amt, paymethod=pay, photo=pic, agree=agree)
            reg.save()
            fm = CustomerRegistration()
            
    else:
        fm = CustomerRegistration()
    cus = User.objects.all()
    return render(request, 'enroll/add_and_show.html', {'cus':cus,'form':fm})

def retrieve_records(request):    
    cus = User.objects.all()
    return render(request, 'enroll/view_records.html', {'cus':cus})

class retrieve_record(ListView):  
    model = User
    def get(self, request):
        fm = CustomerRegistration()
        cus = User.objects.all()
        return render(request, 'enroll/view_records.html', context={'fm':fm, 'cus':cus})

class delete_record(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class update_record(View):
    def get(self, request, id):
        fr = User.objects.get(pk=id)
        fm = CustomerRegistration(instance=fr)
        return render(request, 'enroll/update_customer.html', {'form':fm})

    def post(self, request, id):
        fr = User.objects.get(pk=id)
        fm = CustomerRegistration(request.POST, instance=fr)
        if fm.is_valid():
            fm.save()
        return render(request, 'enroll/update_customer.html', {'form':fm})