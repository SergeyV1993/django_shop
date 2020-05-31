from .models import *
from django.views.generic import *
from django.core.cache import cache


class ProductView(DetailView):
    """Реализация отображения продуктов С ИСПОЛЬЗОВАНИЕМ кэша."""
    model = Product
    template_name = 'product/product.html'
    pk_url_kwarg = 'product_id'

    def get_queryset(self):
        product_id = self.kwargs.get(self.pk_url_kwarg)
        product_key_in_cache = 'product_info_{}'.format(str(product_id))

        if product_key_in_cache in cache:
            return cache.get(product_key_in_cache)

        product_info = self.model.objects\
            .only('name', 'price', 'image', 'description')\
            .filter(pk=product_id)
        cache.set(product_key_in_cache, product_info)

        return product_info


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
