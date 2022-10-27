from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

CATEGORIES = Categories.objects.all().values_list('name', 'name')

class Food(models.Model):
    name = models.CharField(max_length=500)
    category = models.TextField(choices=CATEGORIES)
    price = models.IntegerField()
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='media/food/%y%m%d', blank=True)

    def __str__(self):
        return self.name