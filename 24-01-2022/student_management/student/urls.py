from student import views
from django.urls import path

urlpatterns=[
           path('/', views.student_details, name='student_details'),
           path('student_form/', views.student_registration, name='student_registration'),
           path('staff_form/', views.staff_registration, name='staff_registration'),
          path('staff/', views.staff_details, name='staff_details'),

]
