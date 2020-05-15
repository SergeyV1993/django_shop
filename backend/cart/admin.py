from django.contrib import admin
from .models import *


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.fields]
    search_fields = ['id', 'product__name']

    class Meta:
        model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]
    search_fields = ['id']

    class Meta:
        model = Cart