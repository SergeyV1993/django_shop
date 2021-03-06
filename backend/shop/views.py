from django.views.generic import *
from django.core.cache import cache
from backend.products.models import *


class ShopView(ListView):
    """Реализация отображения всего ассортимента С ИСПОЛЬЗОВАНИЕМ кэша."""
    model = Product
    template_name = 'shop/shop.html'
    paginate_by = 25
    context_object_name = 'products'

    def get_queryset(self):
        if 'products' in cache:
            return cache.get('products')

        products = self.model.objects.only('name', 'price', 'image').filter(is_active=True)
        cache.set('products', products)

        return products


'''
class ShopView(ListView):
    """Реализация отображения всего ассортимента БЕЗ ИСПОЛЬЗОВАНИЕМ кэша."""
    model = Product
    template_name = 'shop/shop.html'
    queryset = model.objects.only('name', 'price', 'image').filter(is_active=True)
    paginate_by = 25
    context_object_name = 'products'
'''

'''
#как запасной вариант для пагинатора
    def get_context_data(self, **kwargs):
        context = super(ShopView, self).get_context_data(**kwargs)
        paginator = Paginator(self.queryset, 25)
        page = self.request.GET.get('page')
        try:
            products_image = paginator.page(page)
        except PageNotAnInteger:
            products_image = paginator.page(1)
        except EmptyPage:
            products_image = paginator.page(paginator.num_pages)

        context['products_image'] = products_image
        return context
'''

'''
# Та же самая реализация, только функцией
from django.shortcuts import render
from django.core.paginator import *

def shop(request):
    products = ProductImage.objects.select_related('product').only('product__name', 'product__price', 'image').filter(is_active=True)

    paginator = Paginator(products, 25)
    page = request.GET.get('page')
    try:
        products_image = paginator.page(page)
    except PageNotAnInteger:
        products_image = paginator.page(1)
    except EmptyPage:
        products_image = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'products_image': products_image,
    }

    return render(request, 'shop/shop.html', context)
'''
