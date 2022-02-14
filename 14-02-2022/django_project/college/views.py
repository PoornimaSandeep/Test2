from django.shortcuts import render, redirect
from .models import college_model
from django.http import HttpResponse
from .forms import college_form



def get_data(request):
    if request.method=='GET':
        data=college_model.objects.all()
        data={'data': data}
        return render(request,'index.html',data)

def insert_data(request):
    form=college_form()
    if request.method=='POST':
        form = college_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("succeesfullyadd")
        else:
            return HttpResponse(form.errors)
    else:
        form = college_form()
        return render(request, "forms.html", {"form": form})
