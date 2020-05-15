from django.urls import path
from backend.home.views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    # для функции
    # path('home/', views.home, name='home'),
    # path('', views.home, name='home'),
    # path('contacts/', views.contacts, name='contacts'),
]
