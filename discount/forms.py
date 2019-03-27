from django import forms


class DiscountForm(forms.Form):
    code = forms.CharField()