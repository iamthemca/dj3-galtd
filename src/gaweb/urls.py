
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import index,portfolio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('portfolio/', portfolio),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

