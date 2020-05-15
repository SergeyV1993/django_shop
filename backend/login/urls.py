from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),

    # для функциональной реализации
    # from django.contrib.auth.views import *
    # path('login/', views.login_view, name='login'),
    # path('change_password/', views.change_password, name='change_password'), # использовать только с вьюхой change_password
]
