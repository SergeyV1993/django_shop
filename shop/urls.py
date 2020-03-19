"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import DefaultRouter
from shop.views import *

router = DefaultRouter()
router.register('api/shop_view', ShopViewSet)

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop_vue/', TemplateView.as_view(template_name='shop/shop_vue.html')),
    # для функции
    # re_path(r'^shop/$', views.shop, name='shop'),
]

urlpatterns += router.urls
