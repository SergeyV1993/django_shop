from django.shortcuts import *
from .forms import UserForm
from django.contrib.auth import *
from django.http import *
from django.views.generic import *


class RegistrationView(CreateView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = 'shop/shop.html'

    def form_valid(self, form):
        new_form = form.save()

        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        new_form.set_password(password)
        new_form.save()
        login_user = authenticate(username=username, password=password)

        if login_user:
            login(self.request, login_user)
            return HttpResponseRedirect(reverse('shop'))
        else:
            return HttpResponseRedirect(reverse('registration'))


'''
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

        context = {
            'form': form,
        }

        return render(request, 'registration/registration.html', context)
'''
