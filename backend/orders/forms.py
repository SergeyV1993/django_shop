from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    customer_email = forms.EmailField(widget=forms.EmailInput)
    customer_name = forms.CharField()
    customer_phone = forms.CharField()

    class Meta:
        model = Order
        fields = ('customer_email', 'customer_name', 'customer_phone')
