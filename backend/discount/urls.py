from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('discount/', csrf_exempt(DiscountView.as_view()), name='discount'),

    # для функциональной реализации
    # from . import views
    # path('discount/', views.discount_view, name='discount'),
]
