from django.conf import settings
from django.db import models
from backend.models import Item
from User.models import User

# Create your models here.

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)