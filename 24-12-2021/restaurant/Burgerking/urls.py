from Burgerking import views
from django.urls import path


urlpatterns= [
   path('home/', views.home, name='home'),
   path('login/', views.login, name='login'),
   path('registration/', views.registration, name='registration'),
   path('logout/', views.logout, name='logout'),
   path('burger/',views.burger,name='burger'),
   path('cart',views.cart,name='cart'),
   path('product',views.product,name='product'),
   path('contactus',views.contactus,name='contactus'),
   path('aboutus',views.aboutus,name='aboutus'),
   path('home_user/',views.home_user,name='home_user'),
   path('product_display/',views.products_display,name='product_display'),
   ]
