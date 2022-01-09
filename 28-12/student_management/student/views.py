from django.shortcuts import render
from .models import Admin,Staff,Student,Course,Subject,Attendence,AttendenceReport,LeaveReportStudent,LeaveReportStaff,FeedBackReportStudent
from .models import FeedBackReportStaff,NotificationStudent,NotificationStaff
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def demo(request):
    return render(request,'demo.html')


def admin(request):
    return render(request,"admin.html")


def staff(request):
    return render(request,"staff.html")

def student(request):
    return render(request,"student.html")

def dashboard2(request):
    return render(request,"index2.html")

def dashboard3(request):
     return render(request,"index3.html")

def registration_admin(request):
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
               return redirect('demo')


    return render(request,'registration.html',{'data':query})


def login(request):
    if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('Password')
         user=auth.authenticate(username=username,password=password)
         if user is not None:
              auth.login(request,user)
              return redirect("demo")
         else:
             messages.info(request,"username password not match")
             return redirect("demo")

    return render(request,'login.html')

def logout(request):
   auth.logout(request)
   return redirect("demo")
