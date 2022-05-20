from django.db import models

class Match(models.Model):
    match_group = models.CharField(("Group"), max_length=1)
    match_date = models.DateField(("Date"))
    match_time = models.TimeField(("Time"))
    team_1 = models.CharField(("Home"), max_length=50)
    team_2 = models.CharField(("Away"), max_length=50)

    def __str__(self):
        return (str(self.pk) + ' ' + self.team_1 + ' vs ' + self.team_2)

    class Meta:
        verbose_name_plural = "Matches"