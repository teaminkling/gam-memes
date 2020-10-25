"""Serializers related to the meme bank."""

from rest_framework import serializers

from meme_bank.models import UserMeme


class UserMemeSerializer(serializers.ModelSerializer):
    """A serializer for `UserMeme`s."""

    class Meta:
        model = UserMeme

        fields = (
            "url",
            "player",
        )
