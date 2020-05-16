from .api import ShopViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/shop_view', ShopViewSet, basename='shop')

urlpatterns = router.urls
