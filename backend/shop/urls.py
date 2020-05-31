from django.urls import path
from .views import *

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    # TODO: позже выпилить
    path('shop_vue/', TemplateView.as_view(template_name='shop/shop_vue.html')),

    # для функциональной реализации
    # path('shop/', views.shop, name='shop'),
]
