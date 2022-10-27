from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
import random
from .forms import AddToCartForm
from .models import CartItem
from foodie.models import Food
from order.models import TestOrder

def generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def index(request):
    if not request.session.get('cart_id'):
        cart_id = generate_cart_id()
        request.session['cart_id'] = cart_id
        print (request.session.values())
    else:
        cart_id = request.session.get('cart_id')

    form = AddToCartForm
    return render(request, 'index.html', {"form":form, 'cart_id':cart_id})

def cart(request):
    if not request.session.get('cart_id'):
        cart_id = generate_cart_id()
        request.session['cart_id'] = cart_id
        print (request.session.values())
    else:
        cart_id = request.session.get('cart_id')

    if request.method == 'POST':
        quantity = request.POST['quantity']
        food = Food.objects.get(id=request.POST['food'])

        print(CartItem.objects.filter(cart_id=cart_id, food=food))

        if CartItem.objects.filter(cart_id=cart_id, food=food).exists():
            return JsonResponse({'detail':'food is already in cart, open the cart to increase the quantity'})
            print('Yes the food is in')

        ci = CartItem()
        ci.cart_id=cart_id
        ci.quantity=quantity
        ci.food=food
        ci.save()
        return redirect('index')

    cart = CartItem.objects.filter(cart_id=cart_id)
    return render(request, 'cart.html', {'cart':cart})

def order(request):
    if request.method == 'POST':
        cart_id = request.session.get('cart_id')
        cart_instance = CartItem.objects.filter(cart_id=cart_id)
        user = request.user

        cart_total = 0
        foods = {}
        for i in cart_instance:
            cart_total += i.total()
            foods[f'{i.name()}']=i.quantity

            print(foods)
            print(cart_total)

        order_instance = TestOrder()
        order_instance.user = user
        order_instance.order = foods
        order_instance.total = cart_total
        order_instance.save()
        print(order_instance)
        
        
    return JsonResponse({'detail':'Sike'})

def remove(request, id):
    if request.method == 'POST':
        food_instance = get_object_or_404(CartItem, id=id)
        food_instance.delete()
        return JsonResponse({'Detail':'Item removed from cart'})

def update_quantity(request, id):
    if request.method == 'POST':
        new_quantity = request.POST['newQuantity']
        food_instance = get_object_or_404(CartItem, id=id)
        food_instance.quantity = new_quantity
        food_instance.save()
        return JsonResponse({'Detail':'Item quantity updated'})

def clear_cart(request):
    cart_id = request.session.get('cart_id')
    cart = CartItem.objects.filter(cart_id=cart_id)
    cart.delete()
    return JsonResponse({'detail':'cart cleared'})

def list_order(request):
    orders = TestOrder.objects.filter(user=request.user)
    return render(request, 'listOrder.html', {'orders':orders})