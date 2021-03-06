"""Viewsets for view behaviour of meme bank models."""

from rest_framework import viewsets

from meme_bank.models import UserMeme
from meme_bank.serializers import UserMemeSerializer


class UserMemeViewSet(viewsets.ModelViewSet):
    """A view set for all the memes created for each game."""

    # FIXME: Permissions here are not correct. #11.

    queryset = UserMeme.objects.all()
    serializer_class = UserMemeSerializer
    http_method_names = ["get", "post"]
