from django.contrib import admin
from django.urls import *
from django.conf.urls.static import static
from django.contrib.auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registration.urls')),
    path('', include('orders.urls')),
    path('', include('products.urls')),
    path('', include('home.urls')),
    path('', include('shop.urls')),
    path('', include('cart.urls')),
    path('', include('categories.urls')),
    path('', include('account.urls')),
    path('', include('login.urls')),
    path('', include('discount.urls')),
    path('', include('search.urls')),

    path(
        'logout/',
        LogoutView.as_view(next_page='shop'),
        name='logout'
    ),

    path(
        'change_password/',
        PasswordChangeView.as_view(
            template_name='password/change_password.html',
            success_url=reverse_lazy('change_password_done')
        ),
        name='change_password'
    ),

    path(
        'change_password_done/',
        PasswordChangeDoneView.as_view(template_name='password/change_password_done.html'),
        name='change_password_done'
    ),

    path(
        'reset_password/',
        PasswordResetView.as_view(
            template_name='password/reset_password.html',
            subject_template_name='password/reset_subject.txt',
            email_template_name='password/reset_body.html',
            success_url=reverse_lazy('reset_password_done')
        ),
        name='reset_password'
    ),

    path(
        'reset_password_done/',
        PasswordResetDoneView.as_view(template_name='password/reset_password_done.html'),
        name='reset_password_done'
    ),

    re_path(
        r'^reset_password_confirmation/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(
            template_name='password/reset_password_confirmation.html',
            success_url=reverse_lazy('reset_password_confirm_done')
            ),
        name='reset_password_confirm'
    ),

    path(
        'reset_password_confirmation_done/',
        PasswordResetCompleteView.as_view(template_name='password/reset_password_confirmation_done.html'),
        name='reset_password_confirm_done'
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

