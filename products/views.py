from cart.models import *
from django.views.generic import *
from django.http import Http404


class ProductView(DetailView):
    model = Product
    template_name = 'product/product.html'
    pk_url_kwarg = 'product_id'

'''
    def get_object(self):
        try:
            product_id = self.kwargs.get('product_id')
            return Product.objects.select_related('type').only('name', 'price', 'description', 'type__name').get(id=product_id)
        except Product.DoesNotExist:
            raise Http404("Product does not exist")

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context
'''

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
