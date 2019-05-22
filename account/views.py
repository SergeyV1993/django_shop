from django.shortcuts import render
from orders.models import *
from django.views.decorators.vary import vary_on_cookie


@vary_on_cookie
def account_view(request):
    if request.user.is_authenticated:
        order = Order.objects.select_related('status').filter(user=request.user).order_by('-id')
        context = {
            'order': order
        }
        return render(request, 'account/account.html', context)
    else:
        return render(request, 'account/account.html', locals())


