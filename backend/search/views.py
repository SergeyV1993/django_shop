from django.shortcuts import render
from backend.orders.models import *
from django.views.generic import *
from django.core.cache import cache


class SearchView(ListView):
    """Реализация поиска продуктов С ИСПОЛЬЗОВАНИЕМ кэша."""
    model = Product
    template_name = 'shop/shop.html'
    paginate_by = 25

    def post(self, request, *args, **kwargs):
        question = self.request.POST.get('search')
        product_key_in_cache = 'products_in_search_{}'.format(str(question))

        if product_key_in_cache in cache:
            search_products = cache.get(product_key_in_cache)
        else:
            search_products = self.model.objects.only('name', 'price', 'image').filter(name__icontains=question)
            cache.set(product_key_in_cache, search_products)

        if search_products:
            context = {
                'products': search_products
            }

            return render(request, self.template_name, context)

        return render(request, 'shop/search.html')
