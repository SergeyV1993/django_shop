from .view import ShopViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('shop', ShopViewSet, basename='shop')

urlpatterns = router.urls
