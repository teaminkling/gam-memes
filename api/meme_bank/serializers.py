"""Serializers related to the meme bank."""

from django_typomatic import ts_interface

from rest_framework import serializers

from meme_bank.models import UserMeme


@ts_interface()
class UserMemeSerializer(serializers.ModelSerializer):
    """A serializer for `UserMeme`s."""

    class Meta:
        model = UserMeme

        fields = (
            "url",
            "player",
        )
