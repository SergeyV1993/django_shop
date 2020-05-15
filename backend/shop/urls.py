from django.urls import path
from backend.shop.views import *
from backend.shop.api import ShopViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop_vue/', TemplateView.as_view(template_name='shop/shop_vue.html')),

    # для функциональной реализации
    # path('shop/', views.shop, name='shop'),
]

"""API"""
router = DefaultRouter()
router.register('api/shop_view', ShopViewSet, basename='shop')
urlpatterns += router.urls
