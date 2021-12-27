from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import fruit


# Create your views here.
def registration(request):
    query=None
    if request.method=='POST':
       username=request.POST.get("username")
       First_name=request.POST.get("Firstname")
       Last_name=request.POST.get("Lastname")
       email=request.POST.get("Email")
       Password=request.POST.get("Password")
       Confirm_password=request.POST.get("confirm_password")
       if Password==Confirm_password:
           if User.objects.filter(username=username).exists():
               messages.info(request,"username already exists")
           elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
           else:
               query=User.objects.create_user(username=username,first_name=First_name,last_name=Last_name,email=email,password=Password)
               query.save()
               return redirect('welcome')


    return render(request,'registration.html',{'data':query})


def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('Password')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
              auth.login(request,user)
              return redirect("welcome")
         else:
             messages.info(request,"username password not match")
             return redirect("login")

    return render(request,'login.html')
def logout(request):
   auth.logout(request)
   return redirect("Home")

def welcome(request):
    total_price=0
    if request.method =='POST':
       fruits=request.POST.get('fruits')
       quantity=int(request.POST.get('quantity'))
       print(quantity)
       total_price=100*quantity

       print(total_price)
    return render(request,'welcome.html',{'data':total_price})


def Home(request):
     return render(request,'home.html')
def cart(request):
    return render(request,'cart.html')
