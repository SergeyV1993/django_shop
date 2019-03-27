from django.shortcuts import render
from cart.models import *


def product(request, product_id):
    product = Product.objects.select_related().get(id=product_id)
    return render(request, 'product/product.html', locals())

