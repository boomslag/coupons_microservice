from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/coupons/', include('apps.coupons.urls')),
    
    path('admin/', admin.site.urls),
]
