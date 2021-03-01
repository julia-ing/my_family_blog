from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']

        user = auth.authenticate(request, username=email, password=pwd)

        if user is None:
            redirect('/join')
        else:
            auth.login(request, user)
            return redirect('/home')

    return render(request, 'join/login.html')

def join(request):
    if request.method == 'POST':
        email = request.POST['email']
        pwd = request.POST['pwd']

        User.objects.create_user(username=email, password=pwd)

        return redirect('/home')
    return render(request, 'join/join.html')

def logout(request):
    auth.logout(request)
    return redirect('/home')
