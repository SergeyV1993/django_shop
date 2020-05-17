from django.contrib import admin
from .models import *


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]
    search_fields = ('id', )
    inlines = [CartItemInline]

    class Meta:
        model = Cart


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CartItem._meta.fields]
    search_fields = ('id', 'product__name', )

    class Meta:
        model = CartItem
