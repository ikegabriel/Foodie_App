from django.test import TestCase
from foodie.models import Food, Categories
from users.models import CustomUser
from rest_framework.authtoken.models import Token

class FoodTestCase(TestCase):
    def setUp(self):
        Food.objects.create(
            name='Rice and Stew',
            category='Regular',
            price=1500,
            quantity=50
            )
        
    def test_food(self):
        rice = Food.objects.get(name='Rice and Stew')
        self.assertEqual(rice.category, 'Regular')

class CategoriesTestCase(TestCase):
    def setUp(self):
        Categories.objects.create(name='Soups')

    def test_category(self):
        cat = Categories.objects.get(name='Soups')
        self.assertEqual(cat.name, 'Soups')

class UserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(
            email='i@g.com',
            password='aaxar12'
        )

    def test_user(self):
        user = CustomUser.objects.get(email='i@g.com')
        self.assertEqual(user.email, 'i@g.com')

class TokenTestCase(TestCase):
    def setUp(self):
        Token.objects.create(
            user='i@g.com',
        )

    def test_user(self):
        testuser = Token.objects.get(user='i@g.com')
        self.assertEqual(testuser.user, 'i@g.com')