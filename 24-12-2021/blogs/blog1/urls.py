from blog1 import views
from django.urls import include, path


urlpatterns=[

path('b1/', views.b1, name='b1'),
path('createpost/', views.createpost, name='createpost'),
path('signin/', views.signin, name='signin'),
path('hello/', views.hello, name='hello'),
path('login/', views.login, name='login'),
]
