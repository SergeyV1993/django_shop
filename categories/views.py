from products.models import *
from django.core.paginator import *
from django.http import Http404
from django.views.generic import *


class CategoryView(DetailView):
    model = ProductCategory
    template_name = 'categories/categories.html'
    pk_url_kwarg = 'categories_id'
    paginate_by = 1

    def get_object(self):
        try:
            catagory_id = self.kwargs.get('categories_id')
            return ProductCategory.objects.get(id=catagory_id)
        except ProductCategory.DoesNotExist:
            raise Http404("Category does not exist")

    def get_context_data(self, **kwargs):
        product = ProductImage.objects.select_related('product').only('product__name', 'product__price',
                                                                      'image').filter(product__type=self.get_object())
        paginator = Paginator(product, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            products_of_category = paginator.page(page)
        except PageNotAnInteger:
            products_of_category = paginator.page(1)
        except EmptyPage:
            products_of_category = paginator.page(paginator.num_pages)

        context = super(CategoryView, self).get_context_data(**kwargs)
        context['categories'] = self.get_object()
        context['products_of_category'] = products_of_category
        return context


'''
#аналогично коду выше только функция
from django.shortcuts import render

def categories(request, categories_id):
    try:
        categories = ProductCategory.objects.get(id=categories_id)
    except ProductCategory.DoesNotExist:
        raise Http404("Category does not exist")

    product = ProductImage.objects.select_related('product').only('product__name', 'product__price', 'image').filter(product__type=categories)

    paginator = Paginator(product, 25)
    page = request.GET.get('page')
    try:
        products_of_category = paginator.page(page)
    except PageNotAnInteger:
        products_of_category = paginator.page(1)
    except EmptyPage:
        products_of_category = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'products_of_category': products_of_category,
    }

    return render(request, 'categories/categories.html', context)
'''