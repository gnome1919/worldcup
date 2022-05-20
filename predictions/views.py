from django.shortcuts import render, redirect
from matches.models import Match
from .forms import UserPredictionForm
from .models import UserPrediction

def user_predictions(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            matches = Match.objects.all()
            return render(request, 'predictions/user_predictions.html',
                          {'matches': matches, 'form': UserPredictionForm()})
        else:
            matches = Match.objects.all()
            for match in matches:
                if request.POST[str(matches)] == True:
                    prediction = UserPrediction
    else:
        return redirect('userlogin')
    # else:
    #     if request.method == 'GET':
    #         return render(request, 'usrauth/signup.html', {'form': UserCreationForm()})
    #     else:
    #         if request.POST['password1'] == request.POST['password2']:
    #             try:                
    #                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) # Creating a user object
    #                 user.save() # Saving the user object to database
    #                 login(request, user)
    #                 return redirect('dashmain')
    #             except IntegrityError:
    #                 return render(request, 'usrauth/signup.html', {'form': UserCreationForm(),
    #                                                             'error': 'Username exists, please choose another one! '})
    #         else:
    #             return render(request, 'usrauth/signup.html', {'form': UserCreationForm(),
    #                                                         'error': 'Password did not match, please try again! '})
