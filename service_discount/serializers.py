from rest_framework import serializers
from discount.models import *


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCart
        fields = ("code")


