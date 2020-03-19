from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_editable = ('is_active',)

    class Meta:
        model = Product
