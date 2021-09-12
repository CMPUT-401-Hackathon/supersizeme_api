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

    def json_representation(self):
        adict = {'category': self.category,
                'serving_size': self.serving_size,
                'calories' : self.calories, 
                'calories_from_fat' : self.calories_from_fat,
                'total_fat' : self.total_fat,
                'saturated_fat' : self.saturated_fat,
                'trans_fat' : self.trans_fat,
                'cholesterol' : self.cholesterol,
                'sodium' : self.sodium,
                'carbohydrates' : self.carbohydrates,
                'fiber' : self.fiber,
                'sugars' : self.sugars,
                'protein' : self.protein
                }
        
        return adict

    def __str__(self):
        return self.name