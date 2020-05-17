from django.core.cache import cache
from django.shortcuts import render
from backend.orders.models import *
from .models import Account
from django.http import *
from django.views.generic import *


class AccountView(ListView):
    """Реализация отображения личного кабинета БЕЗ ИСПОЛЬЗОВАНИЯ кэша"""
    model = Account
    paginate_by = 25
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        account, created = self.model.objects.prefetch_related('order_set').get_or_create(user=request.user)

        context = {
            'account_orders': account.order_set.all(),
        }
        return render(request, self.template_name, context)


class AccountWithCacheView(ListView):
    """Реализация отображения личного кабинета С ИСПОЛЬЗОВАНИЕМ кэша"""
    model = Account
    paginate_by = 25
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)

        if 'account' in cache:
            account_orders = cache.get('account')
        else:
            account_orders, created = self.model.objects.prefetch_related('order_set').get_or_create(user=request.user)
            cache.set('account', account_orders)

        context = {
            'account_orders': account_orders.order_set.all(),
        }
        return render(request, self.template_name, context)


class AccountDeleteView(DeleteView):
    """Удаление личного кабинета"""
    model = Account
    template_name = 'account/account.html'
    success_url = '/'

    def get_object(self):
        account_object = self.model.objects.get(user=self.request.user)
        return account_object

    def get(self, request, *args, **kwargs):
        account_obj = self.get_object()
        user = self.request.user
        account_obj.delete()
        user.delete()
        return HttpResponseRedirect('/')


'''
#Реализация через функции

def account_view(request):
    if request.user.is_authenticated:
        order = Order.objects.select_related('status').filter(user=request.user).order_by('-id').prefetch_related('productinorder_set__product')
        context = {
            'order': order,
        }
        return render(request, 'account/account.html', context)
    else:
        return render(request, 'account/account.html')


def delete_account(request):
    if request.user.is_authenticated:
        order = Order.objects.select_related('status').filter(user=request.user).all()
        order.delete()
        request.user.delete()
        return HttpResponseRedirect("/")
    else:
        return render(request, 'account/account.html')
'''