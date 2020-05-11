from django.urls import path
from .views import *


urlpatterns = [
    path('account/', AccountView.as_view(), name='account'),
    path('account_delete/', AccountDeleteView.as_view(), name='account_delete'),

    # для реализации c применением кэша
    # path('account/', AccountWithCacheView.as_view(), name='account'),

    # для реализации с функциями
    # from account import views
    # path('account/', views.account_view, name='account'),
    # path('account_delete/', views.delete_account, name='account_delete'),
]
