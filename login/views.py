from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Account
# Create your views here.


def register(request):
    if request.method=="POST":
        email= request.POST['email']
        password= request.POST['password']
        if Account.objects.filter(email = email).exists():
            return redirect('login')
        else:
            user = Account.objects.create_user( password = password,email=email)
            auth.login(request,user)
            return redirect('index')
    return render(request,'asset/register.html')

def login(request):
    if request.method=="POST":
        email= request.POST['email']
        if Account.objects.filter(email = email).exists():
            username=Account.objects.filter(email=email)[0].email
        else:
            return redirect('register')
        password= request.POST['password']
        x=auth.authenticate(username=username,password=password)
        if x is not None:
            auth.login(request,x)
            return redirect('index')
        else:
            return redirect('login')
    return render(request,'asset/login.html')


def logout(request):
    return redirect('login')

def index(request):
    content = Account.objects.filter(email = request.user.email)[0]
    context = {
        "content":content,
    }
    return render(request,"asset/index.html",context)
