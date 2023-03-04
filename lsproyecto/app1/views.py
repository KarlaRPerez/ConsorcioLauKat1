from django.shortcuts import render, redirect
from django.views.generic import View
#from django.contrib.auth.forms import UserChangeForm
#from django.contrib.auth.forms import Login
#from django.contrib import messages

# Create your views here.
def Login (request):
    return render(request,"app1/Login.html")

def index (request):
    return render(request,"app1/index.html")

def price  (request):
    return  render(request,"app1/price.html")

def service(request):
    return  render(request,"app1/service.html")

def single (request):
    return  render(request,"app1/single.html")

def about (request):
    return  render(request,"app1/about.html")

def blog (request):
    return  render(request,"app1/blog.html")

def booking (request):
    return  render(request,"app1/booking.html")

def contact (request):
    return  render(request,"app1/contact.html")

#class Vregitro (View):

 #   def get(self ,request):
  #      form = UserChangeForm()
   #     return  render(request,"app1/Login.html",{"form":form})
   
    #def post (self, request):
     #   form =UserChangeForm(request.Post) 
        
      #  if form.is_valid():
            
       #     usuario=form.save()
        
        #    Login(request,usuario)
        
         #   return redirect ('index')
        #else:
          #  for msg in form.error_messages:
           #     messages.error(request,form.error_messages)