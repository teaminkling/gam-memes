"""Models related to game state."""

import random
import string

import logging
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import QuerySet

from data_mine.models import MemeTemplate, MemeTemplateToGameThrough
from .constants import (
    GAME_ROOM_CODE_LENGTH,
    GAME_STATE_CREATING,
    GAME_STATES,
    TOTAL_CODE_REGEN_ATTEMPTS,
    PROHIBITED_ROOM_CODE_WORDS,
)


logger = logging.getLogger(__name__)


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
        primary_key=True,
        unique=True,
        max_length=4,
        verbose_name="Room Key",
        help_text="The unique room key.",
    )

    meme_templates = models.ManyToManyField(
        to="data_mine.MemeTemplate",
        through="data_mine.MemeTemplateToGameThrough",
    )

    #
    # Options
    #

    max_players_allowed = models.PositiveSmallIntegerField(
        verbose_name="Max Players Allowed",
        validators=[MaxValueValidator(32), MinValueValidator(2)],
        help_text="The max amount of allowed players in a game.",
    )

    time_per_turn = models.PositiveSmallIntegerField(
        verbose_name="Time Per Turn",
        validators=[MaxValueValidator(600), MinValueValidator(10)],
        help_text="Number of seconds per turn.",
    )

    max_rounds = models.PositiveSmallIntegerField(
        verbose_name="Maximum Rounds",
        validators=[MaxValueValidator(128), MinValueValidator(1)],
        help_text="The total number of rounds and the final round.",
    )

    #
    # State
    #

    game_started_timestamp = models.DateTimeField(
        auto_now=True,
        verbose_name="Game Started Timestamp",
        help_text=(
            "The timestamp of the room's creation. It is used to calculate when the room should "
            "be deleted."
        ),
    )

    progressing_state_timestamp = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Next State Procs At",
        help_text="The datetime that the state will transition to the next logical state.",
    )

    round = models.PositiveSmallIntegerField(
        default=1,
        validators=[MaxValueValidator(128), MinValueValidator(1)],
        help_text="The current round. This number starts at Round 1 and ends at round MAX.",
    )

    state = models.IntegerField(
        choices=GAME_STATES,
        default=GAME_STATE_CREATING,
        help_text="The current game state, as also reflected in the game clients.",
    )

    @property
    def player_count(self) -> int:
        """
        Get the number of players in this `Game`.

        Notes
        -----
        There is no such property "meme template count" because it will always match the max
        rounds count.

        Returns
        -------
        `int`
            The number of players in this `Game`.
        """

        return Player.objects.filter(game__room_key=self.room_key).count()

    @staticmethod
    def _generate_key() -> str:
        """
        Generate a random key room key.

        Returns
        -------
        `str`
            The key.
        """

        return "".join(
            [random.choice(string.ascii_uppercase) for _ in range(GAME_ROOM_CODE_LENGTH)]
        )

    def save(self, **kwargs):
        # FIXME: If trying to serialize a room code, don't allow it!

        # Handle unique room keys.

        if not self.room_key:
            self.room_key = Game._generate_unique_key()

        # Handle meme templates associated with this game.

        self._add_meme_templates()

        return super().save(**kwargs)

    @staticmethod
    def _generate_unique_key() -> str:
        key: str = Game._generate_key()

        for attempt in range(TOTAL_CODE_REGEN_ATTEMPTS):
            # Keep trying for a key. They can't be a prohibited word nor taken already.

            key_allowed: bool = key not in PROHIBITED_ROOM_CODE_WORDS
            key_unique: bool = not Game.objects.filter(room_key=key).exists()
            if key_allowed and key_unique:
                logger.info("Creating game room with key [%s].", attempt)

                break
            elif attempt == TOTAL_CODE_REGEN_ATTEMPTS - 1:
                raise RuntimeError(
                    f"Game room could not be created. {TOTAL_CODE_REGEN_ATTEMPTS} attempts at "
                    "generating a unique room code have failed. This could mean extremely busy "
                    "servers (need to increase room code count) or a server bug. Please check the "
                    "logs for more information."
                )
            else:
                logger.debug("Room key [%s] attempted but it was taken.", attempt)

            key: str = Game._generate_key()

        return key

    def _add_meme_templates(self) -> None:
        """
        Add meme templates to the `Game`.
        """

        # TODO: This uses a naive purely random selection process. We should include weights.

        templates: QuerySet[MemeTemplate] = MemeTemplate.objects.all().order_by(
            "?"
        )[:self.max_rounds]

        for template in templates:
            MemeTemplateToGameThrough.objects.create(template=template, game=self)

    def __str__(self):
        return f"Game Room ({self.room_key})"


class Player(models.Model):
    """An ephemeral player, tied to a specific `Game` room."""

    name = models.CharField(max_length=256, help_text="A player's chosen name.")

    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)

    ready = models.BooleanField(default=False, help_text="If this player is ready.")

    vip = models.BooleanField(
        default=False,
        verbose_name="VIP",
        help_text="If this player is a VIP of the game they are in.",
    )

    score = models.PositiveIntegerField(
        default=0, help_text="The score this player has."
    )

    def __str__(self):
        return f"Player #{self.id} ({self.name}) of '{self.game}'"

    class Meta:
        unique_together = (("game", "name"),)
