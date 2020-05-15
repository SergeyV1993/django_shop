from django.urls import path
from .views import *

urlpatterns = [
    path('categories/<int:categories_id>/', CategoryView.as_view(), name='categories'),

    # для функциональной реализации
    # from . import views
    # path('categories/<int:categories_id>/', views.categories, name='categories'),
]
