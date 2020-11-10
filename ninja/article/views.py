from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import arti
# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        password=request.POST.get('password','')
        print(name,password)
        user=User.objects.create_user(username=name,password=password)
        user.save()

    return render(request,'article/signup.html')
def loginn(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        password=request.POST.get('password','')
        print(name,password)
        user=authenticate(username=name,password=password)
        if user is not None:
            login(request,user)
            print("you are loged in")
            print(user)
            return redirect('create/')
        else:
            print("invalid  things")
        

    return render(request,'article/login.html')


@login_required(login_url="/login")
def create(request):
    params=arti.objects.filter(cUser=request.user)
    conte={'params':params}
    if request.method=="POST":
        heading=request.POST.get('heading','')
        content=request.POST.get('text','')
        img=request.FILES.get('userimg','')
        user=request.user
        print(content,heading,user)
        con=heading+content
        something='religion'
        if something in con:
            return HttpResponse('your words are not acceptable :cuz:- your words may harm community  or any  person\'s personal feeling.....')
        else:
            messages.info(request,'your article has submitted successfully')
            insert=arti(heading=heading,content=content,cUser=user,somefile=img)
            insert.save()
        
            return redirect('/')
    return render(request,'article/create.html',conte)

