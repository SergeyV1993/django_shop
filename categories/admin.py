from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category
