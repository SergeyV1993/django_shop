from django.shortcuts import render
from cart.models import *


def product(request, product_id):
    product = Product.objects.select_related('type').only('name', 'price', 'description', 'type__name').get(id=product_id)
    return render(request, 'product/product.html', locals())

