from django.db import models
class User(models.Model):
    username = models.CharField(max_length=60)
    age = models.CharField(max_length=60)
    gender = models.IntegerField() # 0 for male, 1 for female, 2 for other
    height = models.IntegerField() # centimeres
    weight = models.IntegerField() # Kgs
    activityLevel = models.IntegerField() # enum
    #TODO: Last 5 Days of Logs

    def __str__(self):
        return self.username