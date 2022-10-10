from unicodedata import category
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    cuisine = models.CharField(max_length=500)