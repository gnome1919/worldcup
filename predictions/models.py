from django.db import models
from django.db import models
from matches.models import Match
from django.contrib.auth.models import User

class UserPrediction(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # team_1 = models.ForeignKey(Matches, to_field="team_1" , on_delete=models.CASCADE)
    # team_2 = models.ForeignKey(Matches, to_field="team_2" , on_delete=models.CASCADE)
    team_1_goals = models.IntegerField()
    team_2_goals = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.pk) + ' ' + self.match.team_1 + ' vs ' + self.match.team_2)