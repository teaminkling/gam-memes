"""Viewsets for view behaviour of data mine models."""

from rest_framework import viewsets

from data_mine.models import MemeTemplate
from data_mine.serializers import MemeTemplateSerializer


class MemeTemplateViewSet(viewsets.ModelViewSet):
    """Viewset for `MemeTemplate`s' API views."""

    queryset = MemeTemplate.objects.all()
    serializer_class = MemeTemplateSerializer
    http_method_names = ["get"]
