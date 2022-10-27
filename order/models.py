from django.db import models
# from foodie.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cart = models.JSONField()
#     date = models.DateField()

class TestOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.JSONField()
    total = models.IntegerField()
    date = models.DateField(auto_now_add=True)