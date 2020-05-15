from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    re_path(
        'activate_regisration/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        ActivateRegistrationView.as_view(),
        name='activate_registration'
    )

    # для функциональной реализации
    # path('registration/', views.registration, name='registration'),
]
