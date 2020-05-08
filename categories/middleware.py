from django.utils.deprecation import MiddlewareMixin
from categories.models import Category


class GetCategory(MiddlewareMixin):
    """Middleware для категорий в шапке base.html"""
    def process_request(self, request):
        category_list = Category.objects.only('name').all()
        request.category_list = category_list
