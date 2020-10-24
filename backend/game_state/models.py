"""Models related to game state."""

import random
import string

from django.db import models

from .constants import (
    GAME_ROOM_CODE_LENGTH,
    GAME_STATE_CREATING,
    GAME_STATES,
    TOTAL_CODE_REGEN_ATTEMPTS,
    PROHIBITED_ROOM_CODE_WORDS,
)


class Game(models.Model):
    """
    An ephemeral game room.

    Notes
    -----
    The `Game` class does not handle self-deletion; other methods must delete game rooms to free
    them for use by other players. There are a total possible 456976 concurrent games not including
    prohibited codes.
    """

    room_key = models.CharField(
        primary_key=True, unique=True, max_length=4, help_text="The unique room key."
    )

    game_started_timestamp = models.DateTimeField(
        auto_now=True,
        help_text=(
            "The timestamp of the room's creation. It is used to calculate when the room should "
            "be deleted."
        ),
    )

    state = models.CharField(
        max_length=64,
        help_text="The current game state, as also reflected in the game clients.",
        choices=GAME_STATES,
        default=GAME_STATE_CREATING,
    )

    @staticmethod
    def create(cls) -> None:
        """
        Create a game with a randomly-generated room key.
        """

        key: str = Game._generate_key()

        for attempt in range(TOTAL_CODE_REGEN_ATTEMPTS):
            # Keep trying for a key. They can't be a prohibited word nor taken already.

            if all([
                key not in PROHIBITED_ROOM_CODE_WORDS,
                not cls.objects.filter(room_key=key).exists(),
            ]):
                break
            elif attempt == TOTAL_CODE_REGEN_ATTEMPTS - 1:
                raise RuntimeError(
                    f"Game room could not be created. {TOTAL_CODE_REGEN_ATTEMPTS} attempts at "
                    "generating a unique room code have failed. This could mean extremely busy "
                    "servers (need to increase room code count) or a server bug."
                )

            key: str = Game._generate_key()

        if not cls.objects.filter(room_key=key).exists():
            cls.objects.create(room_key=key)

    @staticmethod
    def _generate_key() -> str:
        """
        Generate a random key room key.

        Returns
        -------
        `str`
            The key.
        """

        return str(
            random.choice(string.ascii_uppercase) for _ in range(GAME_ROOM_CODE_LENGTH)
        )


class Player(models.Model):
    """An ephemeral player, tied to a specific `Game` room."""

    name = models.CharField(max_length=256, help_text="A player's chosen name.")

    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("game", "name"),)
