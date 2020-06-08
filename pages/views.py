from django.shortcuts import render,redirect,HttpResponse
import time
import datetime
from .models import diary
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    a = datetime.datetime.now()
    b = a.date()
    # print(b)
    context = {
        'b' : b
    }
    return render(request,'pages/index.html',context)

def signup(request):
    if request.method=='POST':
        first_name = request.POST['first-name']
        last_name = request.POST['first-name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repeat_pwd = request.POST['repeat-pwd']
        if password==repeat_pwd:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            user.save()
            return redirect('index')
        else:
            return render(HttpResponse,'password not match')
    return render(request,'pages/signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Enter Valid username and password')

    return render(request,'pages/login.html')

@login_required(login_url='login')
def list(request):
    if User.is_authenticated:
        user = request.user.username 
        print(user)
    data = diary.objects.filter(name=user)
    print(data)
    context = {
        'data' : data
    }
    return render(request,'pages/list.html',context)

@login_required(login_url='login')
def listdisplay(request,pk):
    if request.method == 'POST':
        name = request.POST['name']
        
        a = diary.objects.get(pk=pk)
        a.desc = name
        a.save()
        return redirect('index')

    content = diary.objects.get(pk=pk)
    context = {
        'content' : content
    }
    return render(request,'pages/listdisplay.html',context)

def logout(request):
    auth.logout(request)
    return render(request,'pages/index.html')

@login_required(login_url='login')
def dairy(request):
    a = datetime.datetime.now()
    b = a.date()

    if User.is_authenticated:
        user = request.user.username 
        print(user)

    if request.method=='POST':
        letter = request.POST['letter']
        name = request.POST['name']
        print(name)
        if letter is None:
            messages.error(request,'Enter something in this')
        else:
            Diary = diary (
                desc = letter,
                name = request.user.username
            )
            Diary.save()
    
    content = diary.objects.filter(name=user).filter(date_create=b)
    context = {
        'b' : b,
        'content' : content
    }
    return render(request,'pages/diary.html',context)