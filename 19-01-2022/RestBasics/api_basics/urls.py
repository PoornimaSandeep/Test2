from api_basics import views
from django.urls import path

urlpatterns = [
         path('article_list', views.article_list, name='home'),
         path('article_details/<int:pk>', views.article_details, name='article_details')
]
