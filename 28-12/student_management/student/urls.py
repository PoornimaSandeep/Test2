from student import views
from django.urls import include, path

urlpatterns=  [
path('demo/', views.demo, name='demo'),
path('admin/', views.admin, name='admin'),
path('student/', views.student, name='student'),
path('staff/', views.staff, name='staff'),
path('dashboard3/', views.dashboard3, name='dashboard3'),
path('dashboard2/', views.dashboard2, name='dashboard2'),
path('registration_admin/', views.registration_admin, name='registration_admin'),
path('login/', views.login, name='login'),
path('logout', views.logout, name='logout'),


]
