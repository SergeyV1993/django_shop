from rest_framework.viewsets import ModelViewSet
from products.models import *
from shop.serializers import ShopViewSerializer


class ShopViewSet(ModelViewSet):
    queryset = Product.objects.only('id', 'name', 'price').filter(is_active=True)
    serializer_class = ShopViewSerializer

