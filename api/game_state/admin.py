"""Administrative view objects for game state models."""

from django.contrib import admin

from data_mine.models import MemeTemplateToGameThrough
from game_state.models import Game, Player


class PlayersInGameAdminInline(admin.StackedInline):
    """An inline admin view containing `Player`s for the `Game` Admin view."""

    model = Player

    verbose_name = "Player in this Game"
    verbose_name_plural = "Players in this Game"

    extra = 0


class MemeTemplatesInGameAdminInline(admin.TabularInline):
    """An inline admin view containing `MemeTemplate`s for the `Game` Admin view."""

    model = MemeTemplateToGameThrough

    verbose_name = "Meme Template for this Game"
    verbose_name_plural = "Meme Templates for this Game"

    fields = ("template", "link", "image", "order")
    readonly_fields = (
        "link",
        "image",
    )

    extra = 0

    @staticmethod
    def link(instance: MemeTemplateToGameThrough) -> str:
        """
        A clickable link representation of the provided `MemeTemplate`.

        Parameters
        ----------
        instance : `MemeTemplateToGameThrough`
            The through object.

        Returns
        -------
        `str`
            An HTML URL representation.
        """

        return instance.template.link

    @staticmethod
    def image(instance: MemeTemplateToGameThrough) -> str:
        """
        An image representation of the provided `MemeTemplate`.

        Parameters
        ----------
        instance : `MemeTemplateToGameThrough`
            The through object.

        Returns
        -------
        `str`
            An HTML image representation.
        """

        return instance.template.thumbnail


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin view for the `Game` model."""

    fields = (
        "room_key",
        "vip",
        "max_players_allowed",
        "time_per_turn",
        "max_rounds",
        "game_started_timestamp",
        "progressing_state_timestamp",
        "round",
        "state",
    )

    list_display = (
        "room_key",
        "vip",
        "players",
        "rounds",
        "time_per_turn",
        "game_started_timestamp",
        "state",
    )

    inlines = (
        PlayersInGameAdminInline,
        MemeTemplatesInGameAdminInline,
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # On an edit.

            return "room_key", "game_started_timestamp", "progressing_state_timestamp"

        return "room_key", "game_started_timestamp"

    @staticmethod
    def players(instance: Game) -> str:
        """
        A representation of the current number of players over the maximum number of players.

        Parameters
        ----------
        instance : `Game`
            The `Game` under examination.

        Returns
        -------
        `str`
            The player representation.
        """

        return f"{instance.player_count} / {instance.max_players_allowed}"

    @staticmethod
    def rounds(instance: Game) -> str:
        """
        A representation of the current round, and the max round limit.

        Parameters
        ----------
        instance : `Game`
            The `Game` under examination.

        Returns
        -------
        `str`
            The round representation.
        """

        return f"{instance.round} / {instance.max_rounds}"


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    """Admin view for the `Player` model."""

    fields = (
        "name",
        "ready",
        "vip",
        "score",
        "game",
    )

    list_display = (
        "name",
        "game",
        "ready",
        "vip",
        "score",
    )
