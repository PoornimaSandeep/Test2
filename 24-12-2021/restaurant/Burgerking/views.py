from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Q
from .models import products
from .forms import ProductsForm


# Create your views here.
def home(request):
    return render(request,'home.html')
def home_user(request):
    return render(request,'home_user.html')
def contactus(request):
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def logout(request):
    return redirect('login')

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
               return redirect('home_user')


    return render(request,'registration.html',{'data':query})


def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('Password')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
              auth.login(request,user)
              return redirect("home_user")
         else:
             messages.info(request,"username password not match")
             return redirect("login")

    return render(request,'login.html',{'name' : request.user.username })
'''
def logout(request):
   auth.logout(request)
   return redirect("home")
'''
def welcome(request):
    total_price=0
    if request.method =='POST':
       fruits=request.POST.get('fruits')
       quantity=int(request.POST.get('quantity'))
       print(quantity)
       total_price=100*quantity

       print(total_price)
    return render(request,'welcome.html',{'data':total_price})
def burger(request):
     a=products.objects.all()
     total_price=0
     if request.method =='POST':
        quantity=int(request.POST.get('quantity'))
        print(quantity)
        total_price=100*quantity

        print(total_price)
     return render(request,'burger.html',{'data':total_price,'a':a})



def cart(request):
     total_price=0
     if request.method =='POST':
        quantity=int(request.POST.get('quantity'))
        print(quantity)
        total_price=100*quantity

        print(total_price)
     return render(request,'cart.html',{'data':total_price})

def product(request):
    form=ProductsForm()
    if request.method=='POST':
        f=ProductsForm(request.POST,request.FILES)
        if f.is_valid():
           f.save()
           return redirect("home")

        else:
          return redirect("product")
    else:
        form=ProductsForm()
        return render(request,"products.html",{"form":form})

def products_display(request):
    productss = products.objects.all()
    return render(request, 'p.html', {'productss':productss})
"""
def product(request):
    return redirect("https://www.zomato.com/")
"""
"""
def add_to_cart(request,book_id):
        if request.user.is_authenticated():
            try:
                book = Book.objects.get(pk=book_id)
            except ObjectDoesNotExist:
                pass
            else :
                try:
                    cart = Cart.objects.get(user = request.user, active = True)
                except ObjectDoesNotExist:
                    cart = Cart.objects.create(user = request.user)
                    cart.save()
                    cart.add_to_cart(book_id)
                    return redirect('cart')
                else:
                    return redirect('index')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk = book_id)
        except ObjectDoesNotExist:
            pass 
        else:
            cart = Cart.objects.get(user = request.user, active = True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')
"""