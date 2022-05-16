from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

def usersignup(request):
    if request.user.is_authenticated:
        return redirect('dashlanding')
    else:
        if request.method == 'GET':
            return render(request, 'usrauth/signup.html', {'form': UserCreationForm()})
        else:
            if request.POST['password1'] == request.POST['password2']:
                try:                
                    user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) # Creating a user object
                    user.save() # Saving the user object to database
                    login(request, user)
                    return redirect('dashlanding')
                except IntegrityError:
                    return render(request, 'usrauth/signup.html', {'form': UserCreationForm(),
                                                                'error': 'Username exists, please choose another one! '})
            else:
                return render(request, 'usrauth/signup.html', {'form': UserCreationForm(),
                                                            'error': 'Password did not match, please try again! '})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('dashlanding')            
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
                return redirect('dashlanding')

def userlogout(request):
    # This is needed to neutralize some browser's precache behaviour (Calling logout function which resides in a link)
    if request.method == 'POST':
        logout(request)
        return redirect('home')             