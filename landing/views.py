from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
import datetime as dt
from logging import exception
from matches.models import Match
from django.contrib.auth.models import User
from predictions.models import UserPrediction

# def landing(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')
#     else:
#         return render(request, 'landing/landing.html')

def landing(request):
    predictions = UserPrediction.objects.all()
    users = User.objects.all()
    matches = Match.objects.exclude(result__isnull=True)
    users_total_score = []
    for user in users:
        user_predictions = predictions.filter(user=user, result__isnull=False)
        user_total_score = 0
        user_fullname = user.first_name + ' ' + user.last_name
        for match in matches:            
            user_prediction = user_predictions.filter(match_id=match.id).values('result')[0]['result']
            user_total_score += user_match_score_calc(match, user_prediction)
        users_total_score.append(userTotalScoreDto(user_fullname, user_total_score))
    return render(request, 'landing/landing.html', {'users_total_score':users_total_score})

def user_match_score_calc(match, user_prediction):       
            match_team_1_goals = int(match.result.split(':')[0])
            match_team_2_goals = int(match.result.split(':')[1])
            user_team_1_goals = int(user_prediction.split(':')[0])
            user_team_2_goals = int(user_prediction.split(':')[1])
            if match.result == user_prediction:
                return 10
            if match_team_1_goals != match_team_2_goals:
                if match_team_1_goals - match_team_2_goals == user_team_1_goals - user_team_2_goals:
                    return 7
                if (match_team_1_goals > match_team_2_goals and user_team_1_goals > user_team_2_goals) \
                or (match_team_1_goals < match_team_2_goals and user_team_1_goals < user_team_2_goals):
                    return 5
            else:                    
                if user_team_1_goals == user_team_2_goals:
                    return 3
            return 0

class userTotalScoreDto:
    def __init__(self, user_fullname, user_total_score):
        self.user_fullname = user_fullname
        self.user_total_score = user_total_score