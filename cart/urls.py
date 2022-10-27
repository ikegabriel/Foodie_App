from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('order/', views.order, name='order'),
    path('remove/<int:id>', views.remove, name='remove'),
    path('update_quantity/<int:id>', views.update_quantity, name='update_quantity'),
    path('clear/', views.clear_cart, name='clear'),
    path('orders/', views.list_order, name='orders'),
]