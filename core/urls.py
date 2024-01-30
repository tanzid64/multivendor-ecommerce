from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import BannerApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('banner', BannerApiView, basename='banner-api')

urlpatterns = [
    path('', include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
