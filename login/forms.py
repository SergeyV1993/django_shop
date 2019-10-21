from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):

        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError({'username': 'Такой пользователь не зарегистрирован'}, code='user not exists')

        user = User.objects.get(username=username)
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль')


