from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from .models import Category


class GetCategory(MiddlewareMixin):
    """Middleware для категорий в шапке base.html"""
    def process_request(self, request):
        if 'category_list' in cache:
            category_list = cache.get('category_list')
        else:
            category_list = Category.objects.only('name').all()
            cache.set('category_list', category_list)

        request.category_list = category_list
