from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from . import views, settings
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coleta/', include('coleta.urls')),
    # path('relatorio/', include('relatorio.urls')),
    path('blog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    path('',views.index),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
