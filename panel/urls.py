from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import anasayfa   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anasayfa, name='anasayfa'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)