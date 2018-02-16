from django.urls import path

from django.contrib import admin
from . import views, settings
urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add URLS from the catalog application
from django.conf.urls import include


urlpatterns += [
    path('coleta/', include('coleta.urls')),
    # path('relatorio/', include('relatorio.urls')),
    path('blog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
    path('accounts/', include('allauth.urls')),
    path('$',views.index),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
