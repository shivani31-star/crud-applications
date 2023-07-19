from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['name']) 
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email in db")
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect('/login/')


def login(request):
    return render(request,'login.html')

def table(request):
    data = User.objects.all()
    return render(request,'table.html',{"data":data})

