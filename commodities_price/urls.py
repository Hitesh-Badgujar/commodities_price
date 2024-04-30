
from django.contrib import admin # type: ignore
from django.urls import path,include # type: ignore
from django.conf import settings # type: ignore
from django.conf.url.static import static # type: ignore
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
