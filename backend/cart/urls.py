from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('cart/', csrf_exempt(CartView.as_view()), name='cart_view'),
    path('add_to_cart/', csrf_exempt(AddToCartView.as_view()), name='add_to_cart'),
    path('remove_from_cart/', csrf_exempt(RemoveFromCartView.as_view()), name='remove_from_cart'),

    # для функциональной реализации
    # from . import views
    # path('cart/', views.cart_view, name='cart_view'),
    # path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
]
