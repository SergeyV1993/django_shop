from django.shortcuts import render
from orders.models import *
from django.views.generic import *


class SearchView(ListView):
    model = ProductImage
    template_name = 'shop/shop.html'
    paginate_by = 25

    def post(self, request, *args, **kwargs):
        question = self.request.POST.get('search')

        search = self.model.objects.select_related('product').only(
            'product__name',
            'product__price',
            'image'
        ).filter(product__name__icontains=question)

        if search:
            context = {
                'products_image': search
            }
            return render(request, self.template_name, context)
        return render(request, 'shop/search.html')


