from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .service import account_activation_token, send_email_for_confirm_registration
from .forms import UserForm
from django.contrib.auth import *
from django.http import *
from django.views.generic import *
from django.urls import reverse


class RegistrationView(CreateView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = 'registration/registration_confirmation.html'

    def form_valid(self, form):
        user = form.save()

        password = form.cleaned_data['password1']
        email = form.cleaned_data['email']
        current_domain = get_current_site(self.request)

        user.is_active = False
        user.set_password(password)
        user.save()

        send_email_for_confirm_registration(user, current_domain, email)

        return render(self.request, self.success_url)


class ActivateRegistrationView(View):
    model = User

    def dispatch(self, request, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(kwargs['uidb64']))
            user = self.model.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, kwargs['token']):
            user.is_active = True
            user.save()
            login(request, user)
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
