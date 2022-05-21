# Generated by Django 4.0.4 on 2022-05-21 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField(verbose_name='MatchID')),
                ('match_group', models.CharField(max_length=1, verbose_name='Group')),
                ('match_date', models.DateField(verbose_name='Date')),
                ('match_time', models.TimeField(verbose_name='Time')),
                ('team_1', models.CharField(max_length=50, verbose_name='Home')),
                ('team_2', models.CharField(max_length=50, verbose_name='Away')),
                ('result', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('[0-9]{1,2}:[0-9]{1,2}', message='Wrong input! Ex: 2:0')], verbose_name='Result')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
