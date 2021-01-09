"""Serializers related to game state."""

import logging

from rest_framework import serializers
from rest_framework.fields import CharField

from data_mine.serializers import MemeTemplateSerializer
from game_state.models import Game, Player
from meme_bank.serializers import UserMemeSerializer

logger = logging.getLogger(__name__)


class PlayerSerializer(serializers.ModelSerializer):
    """A serializer for the players."""

    latest_meme = UserMemeSerializer()

    def update(self, instance: Player, validated_data: dict):
        if instance.name != validated_data.get("name"):
            logger.warning(
                "A player's name is not allowed to be changed. Ignoring change request."
            )

            validated_data.pop("name")

        if instance.game != validated_data.get("game"):
            logger.warning(
                "A player's game room cannot be changed post-create. Ignoring change request."
            )

            validated_data.pop("game")

        return super().update(instance, validated_data)

    class Meta:
        model = Player

        fields = (
            "name",
            "game",
            "ready",
            "score",
            "latest_meme",
        )

        read_only_fields = (
            "score",
            "latest_meme",
        )


class GameSerializer(serializers.ModelSerializer):
    """A serializer for the meme templates."""

    meme_templates = MemeTemplateSerializer(many=True, read_only=True)

    vip = PlayerSerializer(read_only=True)

    player_set = PlayerSerializer(many=True, read_only=True)

    vip_name = CharField(
        label="VIP Name",
        min_length=1,
        max_length=512,
        write_only=True,
        help_text="The VIP's name to be created alongside POST requests. Ignored in PUT requests.",
    )

    def create(self, validated_data: dict):
        vip_name: str = validated_data.pop("vip_name")

        # Create the game. It has no VIP.

        game: Game = super().create(validated_data)

        # Create the player from the VIP Name.

        player = Player.objects.create(name=vip_name, game_id=game.room_key)

        # Associate the player as VIP.

        game.vip_id = player.id
        game.save()

        return game

    def update(self, instance: Game, validated_data: dict):
        # Ensure the VIP isn't re-created each time.

        if "vip_name" in validated_data:
            validated_data.pop("vip_name")

        return super().update(instance, validated_data)

    class Meta:
        model = Game

        fields = (
            "room_key",
            "meme_templates",
            "max_players_allowed",
            "time_per_turn",
            "max_rounds",
            "time_until_next_state",
            "round",
            "state",
            "player_set",
            "vip",
            "vip_name",
        )

        read_only_fields = (
            "room_key",
            "meme_templates",
            "time_until_next_state",
            "round",
            "state",
            "player_set",
        )
