from django.shortcuts import render
from .models import user_data
from django.http import HttpResponse
from .service import service_data

# Create your views here.


def first_dose(request):
    if request.method=='POST':
        adhar_no=request.POST.get('adhar')
        name=request.POST.get('name')
        mobile_no=request.POST.get('mobile_no')
        adhar_card=request.POST.get('photo')
        dose='dose1'
        data=user_data(adhar_no=adhar_no,Mobile_no=mobile_no,name=name ,dose=dose,adhar_card=adhar_card)
        data.save()
        return HttpResponse(f'your successfully registered for 1nd dose')
    else:
        return render(request,'register.html')


def sencond_dose(request,adhar_no):
    user=user_data.objects.filter(adhar_no=adhar_no).first()
    if  user_data.objects.filter(adhar_no=adhar_no).first():
        dose='dose2'
        user.adhar_no=user.adhar_no
        user.Mobile_no = user.Mobile_no
        user.name = user.name
        data=user_data(user.adhar_no,user.Mobile_no,user.name ,dose=dose)
        data.save()
        return HttpResponse('you are successfully register for second dose')

    else:
        return HttpResponse('you are not completed first dose please register for Dose1')


def delete_user(request,adhar_no):
    adhar = user_data.objects.filter(adhar_no=adhar_no).delete()
    return HttpResponse(f'data deleted')


def display(request):
    data=user_data.objects.all()
    return render(request,'vaccine_data.html',{'data':data})