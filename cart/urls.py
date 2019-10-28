"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from .views import *

app_name = "cart"
urlpatterns = [
    re_path(r'^cart/$', csrf_exempt(CartView.as_view()), name='cart_view'),
    re_path(r'^add_to_cart/$', csrf_exempt(AddToCartView.as_view()), name='add_to_cart'),
    re_path(r'^remove_from_cart/$', csrf_exempt(RemoveFromCartView.as_view()), name='remove_from_cart'),
    # для функции
    # from . import views
    # re_path(r'^cart/$', views.cart_view, name='cart_view'),
    # re_path(r'^add_to_cart/$', views.add_to_cart, name='add_to_cart'),
    # re_path(r'^remove_from_cart/$', views.remove_from_cart, name='remove_from_cart'),
]
