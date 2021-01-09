"""Viewsets for view behaviour of game state models."""

from rest_framework import viewsets

from game_state.models import Game, Player
from game_state.serializers import GameSerializer, PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    Viewset for `Game`s' API views.

    - GET: For a specific game, get the details of that room.
    - POST: Create a new room.
    - PUT: Update the specific game.
    """

    # FIXME: Permissions are not correct.

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    http_method_names = ["get", "post", "put"]


class PlayerViewSet(viewsets.ModelViewSet):
    """
    Viewset for `Player`s' API views.

    - GET: For a specific player, get their current details.
        - The requesting temporary session's user must be part of the same room as the calling
          player.
    - POST: Create a player given the room they are in.
    - PUT: Update the ready status of the given player.
        - The callee must have a session associated with the specific player under-call.
    """

    # FIXME: Permissions are not correct.

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ["get", "post", "put"]
