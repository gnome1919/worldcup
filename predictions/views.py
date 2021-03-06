import datetime as dt
from logging import exception
from django.shortcuts import render, redirect
from matches.models import Match
from .models import UserPrediction

def user_predictions(request):
    if not request.user.is_authenticated:
        return redirect('user_login')

    match request.method:
        case 'GET':
            context = get_user_prediction(request.user)
            return render(request, 'predictions/user_predictions.html', context)
        case 'POST':
            context = save_user_prediction(request)
            return render(request, 'predictions/user_predictions.html', context)
        case _:
            exception('request method not found')

def get_user_prediction(user):
    user_results = []
    matches = Match.objects.all()
    predictions = UserPrediction.objects.filter(user=user)
    for match in matches:
        try:
            match_datetime = dt.datetime.combine(match.match_date, match.match_time)
            match_datetime = match_datetime - dt.timedelta(hours=3)  
            user_results.append(userPredictionDto(
                matchID=match.id,
                userID=user.id,
                team1_goals=predictions.filter(match_id=match.id).values('result')[0]['result'].split(':')[0],
                team2_goals=predictions.filter(match_id=match.id).values('result')[0]['result'].split(':')[1],
                team1=match.team_1,
                team2=match.team_2,
                isActive=match_datetime >= dt.datetime.now()))
        except IndexError:
            user_results.append(userPredictionDto(
                matchID=match.id,
                userID=user.id,
                team1_goals='',
                team2_goals='',
                team1=match.team_1,
                team2=match.team_2,
                isActive=match_datetime >= dt.datetime.now()))
    return {'user_results': user_results}

def save_user_prediction(respond):
    matches = Match.objects.all()
    for match in matches:
        if respond.POST[str(match.id) + '_team1'] != '' and respond.POST[str(match.id) + '_team2'] != '':
            match_datetime = dt.datetime.combine(match.match_date, match.match_time)
            match_datetime = match_datetime - dt.timedelta(hours=3)           
            if match_datetime < dt.datetime.now():
                return {'error': 'Time is up for one or some of the matches', 'save_tried':True}
            user_result = respond.POST[str(match.id) + '_team1'] + ':' + respond.POST[str(match.id) + '_team2']
            user_prediction, created = UserPrediction.objects.update_or_create(match=match, user=respond.user,
                                        defaults={'match':match, 'user':respond.user, 'result': user_result})

    return {'success': 'Prediction(s) Saved!', 'save_tried':True}

class userPredictionDto:
    def __init__(self, matchID, userID, team1_goals, team2_goals, team1, team2, isActive):
        self.matchID = matchID
        self.userID = userID
        self.team1_goals = team1_goals
        self.team2_goals = team2_goals
        self.team1 = team1
        self.team2 = team2
        self.isActive=isActive