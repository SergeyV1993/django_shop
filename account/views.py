from django.shortcuts import render
from orders.models import *
from django.http import *


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