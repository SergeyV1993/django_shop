from rest_framework import serializers
from backend.account.models import Account


class AccountViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
