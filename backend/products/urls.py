from django.urls import path
from .views import *

urlpatterns = [
   path('product/<int:product_id>/', ProductView.as_view(), name='product'),

   # для функциональной реализации
   # from . import views
   # path('product/<int:product_id>/', views.product, name='product'),
]
