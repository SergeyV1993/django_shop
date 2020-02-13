from cart.models import *
from django.views.generic import *


class ProductView(DetailView):
    model = Product
    template_name = 'product/product.html'
    pk_url_kwarg = 'product_id'


'''
# реализация с помощью функции
from django.shortcuts import render

def product(request, product_id):
    product = Product.objects.select_related('type').only('name', 'price', 'description', 'type__name').get(id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product/product.html', context)
'''
