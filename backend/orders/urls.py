from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('thanks/', CreateOrder.as_view(), name='thanks'),

    # для функциональной реализации
    # from . import views
    # path('checkout/', views.checkout, name='checkout'),
    # path('thanks/', views.make_order, name='thanks'),
]
