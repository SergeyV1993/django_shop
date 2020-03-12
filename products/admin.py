from django.contrib import admin
from .models import *

'''
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory
'''

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_editable = ('is_active',)

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage
