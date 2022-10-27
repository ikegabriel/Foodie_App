from django.db import models
from foodie.models import Food

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    food = models.ForeignKey(Food, unique=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.food.price

    def name(self):
        return self.food.name

    def price(self):
        return self.food.price