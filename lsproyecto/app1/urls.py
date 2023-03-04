from django.urls import path
from app1 import views

urlpatterns = [
    
    path('',views.Login,name="Login"),
    path('index',views.index,name="index"),
    path('service',views.service, name="service"),
    path('single',views.single, name="single"),
    path('about',views.about, name="aboat"),
    path('contact',views.contact,name="contact"),
    path ('price',views.price,name="price"),
    path('booking',views.booking, name="booking"),
    path('blog',views.blog, name="blog"),
   

]
