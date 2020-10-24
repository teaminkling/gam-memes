"""Administrative view objects for game state models."""

from django.contrib import admin

from game_state.models import Game, Player


class PlayersInGameAdminInline(admin.StackedInline):
    """An inline admin view for the `Game` Admin view."""

    model = Player

    verbose_name = "Player in this Game"
    verbose_name_plural = "Players in this Game"

    extra = 0


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin view for the `Game` model."""

    fields = (
        "room_key",
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
        "players",
        "rounds",
        "time_per_turn",
        "game_started_timestamp",
        "state",
    )

    readonly_fields = (
        "game_started_timestamp",
        "progressing_state_timestamp",
    )

    inlines = (
        PlayersInGameAdminInline,
    )

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
