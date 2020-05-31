from django.urls import path
from .views import *


urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('account_delete/', AccountDeleteView.as_view(), name='account_delete'),

    # для функциональной реализации
    # from account import views
    # path('account/', views.account_view, name='account'),
    # path('account_delete/', views.delete_account, name='account_delete'),
]
