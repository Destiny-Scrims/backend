from django.db import models
from djongo import models

# Create your models here.

class User(models.Model):
    member_id = models.CharField(max_length=100)
    access_token= models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)
    expiry_date = models.DateTimeField

