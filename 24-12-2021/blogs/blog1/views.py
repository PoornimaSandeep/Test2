from django.shortcuts import render,redirect
from .models import Post,signup
from .forms import Post_form ,signup_form
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def b1(request):
    a=Post.objects.all()
    b=signup.objects.all()
    return render(request,"blog1.html",{'a':a,'b':b})


def createpost(request):

    form=Post_form()
    if request.method=='POST':
        form=Post_form(request.POST,request.FILES)
        if form.is_valid():
           form.save()

           return redirect("b1")
        else:
          return redirect("b1")
    else:
        form=Post_form()
        img_obj = form.instance
        return render(request,"index.html",{"form":form,'img_obj':img_obj})

def signin(request):

    form=signup_form()
    if request.method=='POST':
        form=signup_form(request.POST,request.FILES)
        if form.is_valid():
           form.save()
           messages.info(request,"Register successfully")
           return redirect("b1")
        else:
          return redirect("b1")
    else:
        form=signup_form()
        return render(request,"signup.html",{"form":form})

def hello(request):
    return render(request,"hello.html")

def login(request):
    data=signup.objects.all()
    query=request.GET.get('r')
    print(query)
    if query is not None:
        #data=data.filter(Q(name=query))
        if query in data:
           data=data.filter(Q(passwoord=query))
           messages.info(request,"INformation based in your input")
        else:
           messages.info(request,"INformation  not based in your input")
    return render(request,"login.html",{"data":data})
