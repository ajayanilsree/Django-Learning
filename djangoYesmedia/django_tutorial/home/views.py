from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
    else:
        form=BookingForm()
    dict_form={
        'form':form,
        'success':True
    }
    return render(request,'booking.html',dict_form)
def doctors(request):
    dict_doct={
        'doct':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doct)
def contact(request):
    return render(request,'contact.html')   
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html', dict_dept)