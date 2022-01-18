from api_basics import views
from django.urls import path

urlpatterns = [
         path('article_list', views.article_list, name='home')
]
