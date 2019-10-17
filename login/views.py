from django.shortcuts import *
from .forms import LoginForm
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.http import *
from .task import send_mail_login

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
                #вызывать аккуратно, только после того как запустил redis-server
                #send_mail_login.delay(username)

                return HttpResponseRedirect(reverse('shop'))
            else:
                return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'login/login.html', context)

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