from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('upload_csv/', views.profile_upload, name='home'),
    path('write_csv/', views.write_csv, name='wrte_csv')
]