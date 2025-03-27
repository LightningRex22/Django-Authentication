from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signUp(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        if password == re_password:
            user = MyUser.objects.create(
                username = email,
                email = email,
                password = password
            )
            return redirect('home')
    return render(request, 'register.html')


def signIn(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email = email, password = password)
        if user is not None:
            login(request, user)
            return HttpResponse('<h1>Login Successful')
        else:
            return HttpResponse('<h1>Login Failed')
    return render(request, 'login.html')