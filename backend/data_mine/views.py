"""Viewsets for view behaviour of data mine models."""

from rest_framework import viewsets

from data_mine.models import MemeTemplate
from data_mine.serializers import MemeTemplateSerializer


class MemeTemplateViewSet(viewsets.ModelViewSet):
    """Viewset for `MemeTemplate`s' API views."""

    # FIXME: This serializer is completely unnecessary. It serves as a good example, though.
    #        What we want is to have a method on the game to pick up N random items rather than
    #        ever calling it from a frontend client.

    # TODO: Also since I'm here: add a link to the API root in grappelli and have proper auth.

    queryset = MemeTemplate.objects.all()
    serializer_class = MemeTemplateSerializer
    http_method_names = ["get"]
