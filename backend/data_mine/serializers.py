"""Serializers related to data mining."""

from rest_framework import serializers

from data_mine.models import MemeTemplate


class MemeTemplateSerializer(serializers.HyperlinkedModelSerializer):
    """A serializer for the meme templates. Expected to only be used for `GET`."""

    def update(self, instance, validated_data):
        raise NotImplementedError("Cannot update meme templates from the serializer.")

    def create(self, validated_data):
        raise NotImplementedError("Cannot create meme templates from the serializer.")

    class Meta:
        model = MemeTemplate

        fields = ("url", "approval_rating")
