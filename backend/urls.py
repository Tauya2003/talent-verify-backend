from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secure/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/auth/', include('core.auth.urls')),
]
