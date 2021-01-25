from django.db import models
from djongo import models
from django import forms

# Create your models here.

class User(models.Model):
    member_id = models.CharField(max_length=100)
    access_token= models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expiry_date = models.DateTimeField()
    displayName = models.CharField(max_length=100)
    membershipId = models.CharField(max_length=100)
    membershipType = models.CharField(max_length=100)
    groupId = models.CharField(max_length=100)
    groupName = models.CharField(max_length=100)

class Team(models.Model):
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player3 = models.CharField(max_length=100)

    class Meta:
        abstract = True

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'player1', 'player2', 'player3'
        )


class Tournament(models.Model):
    member_id = models.CharField(max_length=100)
    numTeams = models.IntegerField()
    teams = models.ArrayField(
        model_container=Team,
        model_form_class=TeamForm
        
        )

    def __str__(self):
        return self.id 

