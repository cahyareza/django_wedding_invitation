"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from myproject.apps.portofolio.views import home


urlpatterns = i18n_patterns(
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("portofolio/", include(("myproject.apps.portofolio.urls", "portofolio"), namespace="portofolio")),
    path('api/', include('myproject.api.urls', namespace='api')),
    path("cart/", include(("myproject.apps.cart.urls", "cart"), namespace="cart")),
    path("order/", include(("myproject.apps.order.urls", "order"), namespace="order")),
    path("cropping/", include(("myproject.apps.cropping.urls", "cropping"), namespace="cropping")),
    path('__debug__/', include('debug_toolbar.urls')),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
