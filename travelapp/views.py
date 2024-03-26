from django.forms import ValidationError
from django.shortcuts import render,redirect
from travelapp.models import Travel_reg,Travel_book 
from travelapp.forms import TravelForm, TravelBookForm
from django.contrib import messages
# Create your views here.



def home(request):
    return render (request,"home.html")

def login(request):
    form = TravelForm(request.POST)
    if request.method == "POST":
        
        username=request.POST.get("username")
        password=request.POST.get("password")
        logincheck=Travel_reg.objects.filter(username=username,password=password)
        if logincheck:
            return redirect('/home')
            
    else:
        form = TravelForm()
        messages.info(request,'Enter valid username or password!')
    return render(request,'login.html',{'form':form})

def book(request):
    if request.method == "POST":
        form = TravelBookForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            return redirect("home")
    else:
        form=TravelBookForm()
    return render(request,'booking.html',{'form':form})

def register(request):
    form = TravelForm(request.POST) 
    if request.method == "POST":
        
        username=request.POST.get("username")
       
        email=request.POST.get("email")
        if Travel_reg.objects.filter(username=username).count()>0:
               txt= messages.info(request,"Username already exists.")  

        elif Travel_reg.objects.filter(email=email).count()>0:
                messages.info(request,"Email already exists.")

        else:
            try:
               
                form.save()
                return redirect('/login')
            except:
                 pass
            
    else:
        form = TravelForm()
    context={
         'form':form,
      
    }
    return render(request,'register.html',context)

def about(request):
    return render(request,'about.html')