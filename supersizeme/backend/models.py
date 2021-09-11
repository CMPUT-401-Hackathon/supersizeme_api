from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    serving_size = models.CharField(max_length=200)
    calories = models.FloatField()
    calories_from_fat = models.FloatField()
    total_fat = models.FloatField()
    saturated_fat = models.FloatField()
    trans_fat = models.FloatField()
    cholesterol = models.FloatField()
    sodium = models.FloatField()
    carbohydrates = models.FloatField()
    fiber = models.FloatField()
    sugars = models.FloatField()
    protein = models.FloatField()