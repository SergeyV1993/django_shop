from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def shop(request):
    products = ProductImage.objects.select_related('product').only('product__name', 'product__price', 'image').filter(is_active=True)
    #categories = ProductCategory.objects.select_related().only('name').all()

    paginator = Paginator(products, 25)
    page = request.GET.get('page')
    try:
        products_image = paginator.page(page)
    except PageNotAnInteger:
        products_image = paginator.page(1)
    except EmptyPage:
        products_image = paginator.page(paginator.num_pages)

    return render(request, 'shop/shop.html', locals())

