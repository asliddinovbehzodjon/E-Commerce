"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from products.views import set_language
urlpatterns = [
    path("set_language/<str:language>", set_language, name="set-language"),
    path('i18n/',include('django.conf.urls.i18n'))
]
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('',include('products.urls'))
)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
INTERNAL_IPS = [
    "127.0.0.1",
]
