from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

def dashmain(request):
    if request.method == 'POST':
        logout(request)
        return redirect('dashmain')
    else:
        return render(request, 'dashboard/dashmain.html')