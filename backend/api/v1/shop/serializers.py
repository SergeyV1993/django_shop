from rest_framework import serializers
from backend.products.models import Product


class ShopViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
