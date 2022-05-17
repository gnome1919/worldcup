from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def landing(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return render(request, 'landing/landing.html')