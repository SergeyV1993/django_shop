from django.urls import *

urlpatterns = [
    path('', include('backend.api.v1.shop.urls')),
]
