from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('account', AccountViewSet, basename='account')
router.register('account_delete', AccountDeleteViewSet, basename='account_delete')

urlpatterns = router.urls
