from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request,"users/user.html")
    
def login_view(request):
    if(request.method == "POST"):
        username=request.POST["username"]
        password=request.POST["password"]
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            print("not logging yo why the hell it isnt showing")
            return render(request,"users/login.html",{
                'message':"Invalid credentials"
            })
    
    return render(request,"users/login.html") 

def logout_view(request):
    username="not defined username"
    if request.user.is_authenticated:
        username=request.user.first_name
    logout(request)
    return render(request,"users/login.html",{
        "message":"logged out",
        "username":username,

    })