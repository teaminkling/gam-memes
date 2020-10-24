"""Root URL config for the entire server application."""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from data_mine.views import MemeTemplateViewSet

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("admin/", admin.site.urls),
]

# The contrib has been added so now add the custom Django Rest Framework viewsets via routers:

router = routers.DefaultRouter()

router.register(r"meme_templates", MemeTemplateViewSet)

urlpatterns += [
    path("api/", include(router.urls)),
]
