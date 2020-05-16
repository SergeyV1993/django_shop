from django.urls import *

urlpatterns = [
    path('api/v1/', include('backend.api.v1.shop.urls')),
    path('api/v1/', include('backend.api.v1.account.urls')),
]
