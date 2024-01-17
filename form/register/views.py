from django.shortcuts import render,redirect
from . forms import CreateUserForm,loginform

#authemtication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'register/index.html')

def register(request):
     form=CreateUserForm()
     if request.method == 'POST':
          form=CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect("login")  
     context={'registerform':form}
     return render(request, 'register/register.html',context=context)

def login(request):
     form=loginform()
     if request.method == 'POST':
          form=loginform(request,data=request.POST)
          if form.is_valid():
               username=request.POST.get('username')
               password=request.POST.get('password')
               
               user=authenticate(request,username=username,password=password)
               
               if user is not None:
                    auth.login(request,user)
                    return redirect("dashboard")
               
     context={'loginform':form}
     
     return render(request, 'register/login.html',context=context)

def logout(request):
     auth.logout(request)
     return redirect("")

@login_required(login_url='my_login')
def dashboard(request):
     return render(request, 'register/dashboard.html')