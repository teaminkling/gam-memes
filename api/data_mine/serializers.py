"""Serializers related to data mining."""

import os

from django_typomatic import ts_interface

from django.conf import settings
from rest_framework import serializers

from data_mine.models import MemeTemplate


@ts_interface()
class MemeTemplateSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for the meme templates. Expected to only be used for `GET`."""

    def update(self, instance, validated_data):
        raise NotImplementedError("Cannot update meme templates from the serializer.")

    def create(self, validated_data):
        raise NotImplementedError("Cannot create meme templates from the serializer.")

    class Meta:
        model = MemeTemplate

        fields = ("url", "likes", "dislikes")



