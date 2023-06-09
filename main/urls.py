from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

from .yasg import urlpatterns as doc_urls
from . import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Russia
    path('', include('apps.expo_app.urls')),
    path('', include('apps.main_page.urls')),
    path('', include('apps.members.urls')),
    path('', include('apps.registration.urls')),
    # English
    path('', include('apps_en.expo_app_en.urls')),
    path('', include('apps_en.main_page_en.urls')),
    path('', include('apps_en.members_en.urls')),
    path('', include('apps_en.registration_en.urls')),
] 

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)