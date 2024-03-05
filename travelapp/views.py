from django.shortcuts import render,redirect
from travelapp.models import Travel_reg,Travel_book 
from travelapp.forms import TravelForm
# Create your views here.



def home(request):
    return render (request,"home.html")

def login(request):
    if request.method == "POST":
        form = TravelForm(request.POST) 
        if form.is_valid():
            
            form.save()
            return redirect('/home')
            
    else:
        form = TravelForm()
    return render(request,'login.html',{'form':form})

def book(request):
    pass

def register(request):
    if request.method == "POST":
        form = TravelForm(request.POST) 
        if form.is_valid():
            
            form.save()
            return redirect('/home')
            
    else:
        form = TravelForm()
    return render(request,'login.html',{'form':form})