
from django.urls import path
from . import views

urlpatterns = [

     path('firstdose', views.first_dose, name='first_dose'),
     path('second_dose/<int:adhar_no>', views.sencond_dose, name='second_dose'),
     path('delete/<int:adhar_no>', views.delete_user, name='register'),
     path('display', views.display, name='display')

]