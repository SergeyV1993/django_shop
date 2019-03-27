from django.shortcuts import render
from products.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def categories(request,categories_id):
    categories = ProductCategory.objects.get(id=categories_id)
    product = Product.objects.select_related('type').filter(type=categories)

    paginator = Paginator(product, 25)
    page = request.GET.get('page')
    try:
        products_of_category = paginator.page(page)
    except PageNotAnInteger:
        products_of_category = paginator.page(1)
    except EmptyPage:
        products_of_category = paginator.page(paginator.num_pages)

    return render(request, 'categories/categories.html', locals())
