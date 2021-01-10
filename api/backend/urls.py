"""Root URL config for the entire server application."""

import os

from django_typomatic import generate_ts

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from data_mine.views import MemeTemplateViewSet
from game_state.views import GameViewSet, PlayerViewSet
from meme_bank.views import UserMemeViewSet

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]

# The contrib has been added so now add the custom Django Rest Framework viewsets via routers:

router = routers.DefaultRouter()

router.register(r"game", GameViewSet)
router.register(r"player", PlayerViewSet)
router.register(r"templates", MemeTemplateViewSet)
router.register(r"memes", UserMemeViewSet)

urlpatterns += [
    path("api/", include(router.urls)),
]

generate_ts(os.path.join(settings.TYPESCRIPT_MODEL_OUTPUT, "_auto_type.ts"))
