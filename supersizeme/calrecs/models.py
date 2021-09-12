# models.py
from django.db import models
class User(models.Model):
    username = models.CharField(max_length=60)
    age = models.CharField(max_length=60)
    gender = models.IntegerField()
    height = models.IntegerField() #centimeres
    weight = models.IntegerField() # Kgs
    activityLevel = models.IntegerField() #enum
    
    def __str__(self):
        return self.name