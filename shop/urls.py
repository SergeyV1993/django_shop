from django.urls import path
from shop.views import *
from rest_framework.routers import DefaultRouter
from shop.api import ShopViewSet

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop_vue/', TemplateView.as_view(template_name='shop/shop_vue.html')),
    # For function
    # path('shop/', views.shop, name='shop'),
]

"""For API"""
router = DefaultRouter()
router.register('api/shop_view', ShopViewSet, basename='shop')
urlpatterns += router.urls
