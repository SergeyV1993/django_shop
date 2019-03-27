from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    customer_email = forms.EmailField(required=True,)
    customer_name = forms.CharField(required=True,)
    customer_phone = forms.CharField(required=True,)

    class Meta:
        model = Order
        fields = ['customer_email', 'customer_name', 'customer_phone']



