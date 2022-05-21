from django.db import models
from django.core.validators import RegexValidator

class Match(models.Model):
    match_id = models.IntegerField(("MatchID"))
    match_group = models.CharField(("Group"), max_length=1)
    match_date = models.DateField(("Date"))
    match_time = models.TimeField(("Time"))
    team_1 = models.CharField(("Home"), max_length=50)
    team_2 = models.CharField(("Away"), max_length=50)
    result = models.CharField(("Result"), blank=True, null=True, max_length=5,
                              validators=[RegexValidator('[0-9]{1,2}:[0-9]{1,2}', message="Wrong input! Ex: 2:0")])

    def __str__(self):
        return (str(self.pk) + ' ' + self.team_1 + ' vs ' + self.team_2)

    class Meta:
        verbose_name_plural = "Matches"