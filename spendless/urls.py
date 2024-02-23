
from django.contrib import admin
from django.urls import path,include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authentications/', include('authentications.urls')),
    # path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('accounts/', include('allauth.urls')),
]
