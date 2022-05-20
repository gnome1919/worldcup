
from django.forms import ModelForm
from .models import UserPrediction

class UserPredictionForm(ModelForm):
    class Meta:
        model = UserPrediction
        fields = ['match', 'team_1_goals', 'team_2_goals']