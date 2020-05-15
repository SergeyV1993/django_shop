from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError({'username': 'Такой пользователь уже существует'}, code='user exists')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError({'email': 'Такой email уже существует'}, code='email exists')

