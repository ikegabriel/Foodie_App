from django.shortcuts import get_object_or_404, render
from foodie.models import Food
from .serializers import *
from cart.models import CartItem
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser


import random

User = get_user_model()

def generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def documentation(request):
    return render(request, 'documentation.html', {})

# Lists all of the food
class ListFoodView(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=200)

# Lists details of a single food
class FoodDetailView(APIView):

    # Fetch Food instance using id
    def get_object(self, id):
        try:
            return Food.objects.get(id=id)
        except Food.DoesNotExist:
            return None

    def get(self, request, id):
        food = self.get_object(id)

        if not food:
            return Response({'error':'The object with the food id does not exist'}, status=400)

        serializer = FoodSerializer(food)
        return Response(serializer.data, status=200)

# Handles adding to the cart and displaying the current cart items
class Cart(APIView):
    
    def get(self, request):
        if not request.session.get('cart_id'):
            cart_id = generate_cart_id()
            request.session['cart_id'] = cart_id
            print (request.session.values())
        else:
            cart_id = request.session.get('cart_id')
        
        cart = CartItem.objects.filter(cart_id=cart_id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        if not request.session.get('cart_id'):
            cart_id = generate_cart_id()
            request.session['cart_id'] = cart_id
            print (request.session.values())
        else:
            cart_id = request.session.get('cart_id')
        
        data = JSONParser().parse(request)
        food_instance = Food.objects.get(id=int(data['food']))

        cart_item = CartItem()
        cart_item.cart_id = cart_id
        cart_item.food = food_instance
        cart_item.quantity = int(data['quantity'])
        cart_item.save()

        serializer = CartSerializer(cart_item, many=True)
        return Response(serializer.data, status=200)

# Increase or reduce the quantity of an item in the cart
class EditQuantity(APIView):
    def get_object(self, id, cart_id):
        try:
            return CartItem.objects.get(cart_id=cart_id, id=id)
        except CartItem.DoesNotExist:
            return None

    def post(self, request, id):
        cart_id = request.session.get('cart_id')
        cart_instance = self.get_object(id=id, cart_id=cart_id)

        if cart_instance == None:
            return Response({'error':'The Item with object id does not exist'}, status=400)

        data = JSONParser().parse(request)

        cart_instance.quantity = data['quantity']
        cart_instance.save()

        serializer = CartSerializer(cart_instance)
        return Response(serializer.data, status=200)

# Remove an item from the cart
class RemoveCartItem(APIView):
    def get_object(self, id, cart_id):
        try:
            return CartItem.objects.get(cart_id=cart_id, id=id)
        except CartItem.DoesNotExist:
            return None
    def delete(self, request, id):
        cart_id = request.session.get('cart_id')
        cart_instance = self.get_object(id=id, cart_id=cart_id)
        
        if cart_instance == None:
            return Response({'error':'The Item with object id does not exist'}, status=400)

        cart_instance.delete()
        cart = CartItem.objects.filter(cart_id=cart_id)
        serializer = CartSerializer(cart, many=True)

        return Response(serializer.data, status=200)
        
# Clear the whole cart
class ClearCart(APIView):
    def get_object(self, cart_id):
        try:
            return CartItem.objects.filter(cart_id=cart_id)
        except CartItem.DoesNotExist:
            return None
    def delete(self, request):
        cart_id = request.session.get('cart_id')
        cart = self.get_object(cart_id)

        if cart == None:
            return Response({'error':'The Item with object id does not exist'}, status=400)
        
        cart.delete()

        cart = CartItem.objects.filter(cart_id=cart_id)
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data, status=200)