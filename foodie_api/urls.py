from django.urls import path
from . import views
urlpatterns = [
    path('', views.documentation, name='home'),
    path('foods/', views.ListFoodView.as_view(), name='foods'),
    path('foods/<int:id>/', views.FoodDetailView.as_view(), name='food'),
    path('cart/', views.Cart.as_view(), name='cart'),
    path('cart/', views.Cart.as_view(), name='add'),
    path('quantity/<int:id>/', views.EditQuantity.as_view(), name='quantity'),
    path('remove/<int:id>/', views.RemoveCartItem.as_view(), name='remove'),
    path('clear/', views.ClearCart.as_view(), name='clear'),
]