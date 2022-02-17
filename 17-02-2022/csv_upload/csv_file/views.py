import csv, io
import logging

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .form import EventsForm
import csv
import pandas as pd
from .models import Profile


def profile_upload(request):
    if request.method=='POST':
       file=request.FILES['file']
       csv_file=file.read().decode("utf-8")
       data_file=csv_file.split("\r\n")
       l2=[]
       count=0
       for i in data_file:
           data=i.split(",")
           l2.append(data)

       for i in range(len(l2)):
           f_data=l2[i]
           for j in range(len(f_data)):
               if j==0:
                  email=f_data[j]
               if j == 1:
                   user_name = f_data[j]
               if j == 2:
                   password = f_data[j]
               if j == 3:
                   first_name = f_data[j]
               if j == 4:
                   last_name = f_data[4]

           staff=Profile(email=email,username=user_name,password=password,Firstname=first_name,Lastname=last_name)
           staff.save()
       return HttpResponse("success")

    else:
        return render(request,'profile.html')


def write_csv(request):
    file_write=open('details.csv','w')
    data=Profile.objects.all()
    context = {
        "data": data
    }
    for i in data:
        file_write.write(i.email)
        file_write.write(",")
        file_write.write(i.username)
        file_write.write(",")
        file_write.write(i.password)
        file_write.write(",")
        file_write.write(i.Firstname)
        file_write.write(",")
        file_write.write(i.Lastname)
        file_write.write(",")
        file_write.write("\n")

    return render(request,"writecsv.html",context)
