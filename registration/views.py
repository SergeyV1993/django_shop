from django.shortcuts import *
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.http import *


def registration(request):
    form = UserForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            new_form = form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            new_form.set_password(password)
            new_form.save()
            login_user = authenticate(username=username, password=password)

            if login_user:
                login(request, login_user)
                return HttpResponseRedirect(reverse('shop'))
            else:
                return HttpResponseRedirect(reverse('registration'))
        else:
            return HttpResponseRedirect(reverse('registration'))
    else:
        form = UserForm()

    return render(request, 'registration/registration.html', locals())
