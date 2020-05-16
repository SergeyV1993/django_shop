from rest_framework import serializers
from backend.orders.models import Order


class AccountViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
