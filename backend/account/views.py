from django.core.cache import cache
from django.shortcuts import render
from backend.orders.models import *
from django.http import *
from django.views.generic import *


class AccountView(ListView):
    """Реализация отображения личного кабинета БЕЗ ИСПОЛЬЗОВАНИЯ кэша"""
    model = Order
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        order = self.model.objects.select_related('status').filter(user=request.user).order_by(
            '-id').prefetch_related('productinorder_set__product')

        context = {
            'order': order,
        }
        return render(request, self.template_name, context)


class AccountWithCacheView(ListView):
    """Реализация отображения личного кабинета С ИСПОЛЬЗОВАНИЕМ кэша"""
    model = Order
    template_name = 'account/account.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, self.template_name)

        if 'order' in cache:
            order = cache.get('order')
        else:
            order = self.model.objects.select_related('status').filter(user=request.user).order_by(
                '-id').prefetch_related('productinorder_set__product')
            cache.set('order', order)

        context = {
            'order': order,
        }
        return render(request, self.template_name, context)


class AccountDeleteView(DeleteView):
    """Удаление личного кабинета"""
    model = Order
    template_name = 'account/account.html'
    success_url = '/'

    def get_object(self):
        order_objects = self.model.objects.select_related('status').filter(user=self.request.user).all()
        return order_objects

    def get(self, request, *args, **kwargs):
        orders_obj = self.get_object()
        user = self.request.user
        orders_obj.delete()
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