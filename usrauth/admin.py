from django.contrib import admin
from matches.models import Match
from predictions.models import UserPrediction

admin.site.register([Match, UserPrediction])