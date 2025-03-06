
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from conf import settings
from home.views import home_page

urlpatterns = [
    path('',home_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)