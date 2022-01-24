from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student,staff
from .forms import student_form,staff_form
# Create your views here.


def student_details(request):
    data=student.objects.all()
    return render(request,'student_details.html',{'data':data})

def staff_details(request):
    data=staff.objects.all()
    return render(request,'staff_details.html',{'data':data})

def student_registration(request):
    form = student_form()
    if request.method == 'POST':
        f = student_form(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect("student_details")

        else:
            return redirect("student_registration")
    else:
        form = student_form()
        return render(request, "student_form.html", {"form": form})

def staff_registration(request):
    form = staff_form()
    if request.method == 'POST':
        f = staff_form(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect("staff_details")

        else:
            return redirect("staff_registration")
    else:
        form = staff_form()
        return render(request, "student_form.html", {"form": form})

