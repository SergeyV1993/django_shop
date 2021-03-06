from .models import *
from backend.products.models import Product
from django.core.paginator import *
from django.http import Http404
from django.views.generic import *
from django.core.cache import cache


class CategoryView(DetailView):
    """Реализация отображения продуктов в категориях С ИСПОЛЬЗОВАНИЕМ кэша."""
    model = Category
    template_name = 'categories/categories.html'
    pk_url_kwarg = 'categories_id'
    paginate_by = 25

    def get_object(self, **kwargs):
        try:
            category_id = self.kwargs.get('categories_id')
            category_key_in_cache = 'category_{}'.format(str(category_id))

            if category_key_in_cache in cache:
                return cache.get(category_key_in_cache)

            category = Category.objects.prefetch_related('product_set').get(id=category_id)
            cache.set(category_key_in_cache, category)

            return category

        except Category.DoesNotExist:
            raise Http404("Category does not exist")

    def get_context_data(self, **kwargs):

        product = Product.objects\
            .only('name', 'price', 'image')\
            .filter(type=self.get_object())\
            .order_by('name')

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
        categories = Category.objects.get(id=categories_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    product = Product.objects.only('name', 'price', 'image').filter(type=categories)

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