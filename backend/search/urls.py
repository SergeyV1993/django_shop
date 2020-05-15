from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('search/', csrf_exempt(SearchView.as_view()), name='search'),
]
