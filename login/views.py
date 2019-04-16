from django.shortcuts import *
from .forms import LoginForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.http import *
from django.core.mail import send_mail
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib import messages
#from django.contrib.auth.decorators import login_required


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login_user = authenticate(username=username, password=password)
            if login_user:
                login(request, login_user)

                subject = 'Авторизация на сайте'
                message = 'Выполнен вход'
                send_mail(subject, message, 'sergey.vlasov333@gmail.com', ['sergey.vlasov333@yandex.ru'])

                return HttpResponseRedirect(reverse('shop'))
            else:
                return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()
    return render(request, 'login/login.html', locals())

'''
#как альтернативный вариант PasswordChangeView
@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('shop'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'password/change_password.html', locals())
'''