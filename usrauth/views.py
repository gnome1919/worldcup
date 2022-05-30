from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
from .forms import SignUpForm

def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, 'User registration successful')
                return redirect('dashmain')
        else:
            form = SignUpForm()
        return render(request, 'usrauth/signup.html', {'form': form})                                                            
    return redirect('dashmain')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashmain')            
    else:
        if request.method == 'GET':
            return render(request, 'usrauth/login.html', {'form': AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user == None:
                return render(request, 'usrauth/login.html', {'form': AuthenticationForm(),
                                                           'error': 'Username or password is wrong, please try again! '})
            else:
                login(request, user)
                return redirect('dashmain')

def user_logout(request):
    #(?) This is needed to neutralize some browser's precache behaviour (Calling logout function which resides in a link)
    # if request.method == 'POST':
    logout(request)
    return redirect('landing')             