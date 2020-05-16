from django.urls import path
from backend.shop.views import *

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop_vue/', TemplateView.as_view(template_name='shop/shop_vue.html')),

    # для функциональной реализации
    # path('shop/', views.shop, name='shop'),
]
