from django.urls import re_path
from .view import *

urlpatterns = [
    re_path(r'^api/v1/code/$', Discounts.as_view()),
]