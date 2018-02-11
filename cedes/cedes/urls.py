"""cedes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from. import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Use include() to add URLS from the catalog application
from django.conf.urls import include

urlpatterns += [
    url(r'^coleta/', include('coleta.urls')),
    # url(r'^relatorio/', include('relatorio.urls')),
    # url(r'^dynamic_forms/',include('dynamic_forms.urls', namespace='dynamic_forms')),
    # url(r'^forms/', include('forms_builder.forms.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$',views.index),    
]
