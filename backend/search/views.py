from django.shortcuts import render
from backend.orders.models import *
from django.views.generic import *


class SearchView(ListView):
    model = Product
    template_name = 'shop/shop.html'
    paginate_by = 25

    def post(self, request, *args, **kwargs):
        question = self.request.POST.get('search')

        search_products = self.model.objects.only('name', 'price', 'image').filter(name__icontains=question)

        if search_products:
            context = {
                'products': search_products
            }
            return render(request, self.template_name, context)
        return render(request, 'shop/search.html')


