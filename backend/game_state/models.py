import random
import string

from django.db import models

from game_state.constants import GAME_ROOM_CODE_LENGTH, GAME_STATES


class Game(models.Model):
    """An ephemeral game room."""

    room_key = models.CharField(
        primary_key=True, unique=True, max_length=4, help_text="The unique room key."
    )

    # FIXME: Room deletion is not yet implemented. It must be implemented before release date to the internet.

    game_started_timestamp = models.DateTimeField(
        auto_now=True,
        help_text="The timestamp of the room's creation, used to calculate when the room should be deleted.",
    )

    state = models.CharField(
        max_length=64, help_text="The current state of the game.", choices=GAME_STATES,
    )

    @classmethod
    def create(cls):
        """
        Create a game with a randomly-generated room key.

        TODO
        -----
        There are some curse words here that might not be streamer friendly. This should be filterable.
        """

        key: str = "".join(
            random.choice(string.ascii_uppercase) for _ in range(GAME_ROOM_CODE_LENGTH)
        )

        cls.objects.create()


class Player(models.Model):
    """An ephemeral player, tied to a specific `Game` room."""

    name = models.CharField(max_length=256, help_text="A player's chosen name.")

    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("game", "name"),)
