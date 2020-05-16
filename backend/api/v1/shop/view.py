from rest_framework.viewsets import ReadOnlyModelViewSet
from backend.products.models import *
from .serializers import ShopViewSerializer


class ShopViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.only('id', 'name', 'price').filter(is_active=True)
    serializer_class = ShopViewSerializer
