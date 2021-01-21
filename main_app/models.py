from django.db import models
from djongo import models

# Create your models here.



class User(models.Model):
    member_id = models.CharField(max_length=100)
    access_token= models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expiry_date = models.DateTimeField
    displayName = models.CharField
    membershipId = models.CharField
    membershipType = models.CharField
    groupId = models.CharField
    groupName = models.CharField



class Team(models.Model):
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player3 = models.CharField(max_length=100)


class Tournament(models.Model):
    member_id = models.CharField(max_length=100)
    numTeams = models.IntegerField

    
    
   
