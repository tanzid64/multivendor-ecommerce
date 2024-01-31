from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('user.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
