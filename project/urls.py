"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('', include('orders.urls')),
    path('', include('products.urls')),
    path('', include('home.urls')),
    re_path('', include('shop.urls')),
    re_path('', include('cart.urls')),
    re_path('', include('categories.urls')),
    re_path('', include('account.urls')),
    re_path('', include('login.urls')),
    re_path('', include('discount.urls')),
    re_path(r'^logout/$', LogoutView.as_view(next_page='shop'), name='logout'),
    re_path(r'^change_password/$', PasswordChangeView.as_view(template_name='password/change_password.html', success_url=reverse_lazy('change_password_done')), name='change_password'),
    re_path(r'^change_password_done/$', PasswordChangeDoneView.as_view(template_name='password/change_password_done.html'), name='change_password_done'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

