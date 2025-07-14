"""
URL configuration for webcafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from core import views
from services import views
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("core.urls")),
    path('admin/', admin.site.urls),
    path('services/', include("services.urls")),
    path('blog/', include("blog.urls")),
    path('pages/', include (('pages.urls','pages'), namespace='pages')),
    path('contact/', include("contact.urls")),
    path('store/', include("visitanos.urls")),  # Cambiado de 'visitanos/' a 'store/'
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)