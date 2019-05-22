from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.vary import vary_on_cookie


@vary_on_cookie
def shop(request):
    products = ProductImage.objects.select_related('product').filter(is_active=True)
    categories = ProductCategory.objects.select_related().only('name').all()

    paginator = Paginator(products, 25)
    page = request.GET.get('page')
    try:
        products_image = paginator.page(page)
    except PageNotAnInteger:
        products_image = paginator.page(1)
    except EmptyPage:
        products_image = paginator.page(paginator.num_pages)

    return render(request, 'shop/shop.html', locals())

