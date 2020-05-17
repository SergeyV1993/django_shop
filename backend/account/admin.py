from django.contrib import admin
from .models import *
from backend.orders.models import Order


class OrdersInline(admin.TabularInline):
    model = Order
    extra = 0


@admin.register(Account)
class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]
    search_fields = ('id', )
    inlines = [OrdersInline]

    class Meta:
        model = Account
