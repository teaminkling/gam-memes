"""Authenticated views used to monitor, mutate, and administrate game state."""

from django.http import HttpRequest, HttpResponse
from django.views import View


class JoinRoomView(View):
    """View for a player client joining a room using basic (insecure) authentication."""

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Attempt to join the room given some player details, granting the current user a session.

        The types of outcomes are:

        - Success! Username: not taken and room code exists.
        - Failure! Username: taken, but the room code exists.
        - Failure! The room code does not exist.
        - Failure! You've been rate limited.

        Parameters
        ----------
        request: `HttpRequest`
            The `HttpRequest`.

        Returns
        -------
        `HttpResponse`
            JSON response for after the user attempts to join the game.
        """

        pass


class CreateRoomView(View):
    """View for a player client creating a room. This player will become the VIP of that room."""

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Attempt to create a room and return a payload that mutates the client's state.

        The types of outcomes are:

        - Success: Successfully created room.
        - Failure: There are no more rooms left (meaning somehow there are 400k+ rooms concurrently).

        Parameters
        ----------
        request: `HttpRequest`
            The `HttpRequest`.

        Returns
        -------
        `HttpResponse`
            JSON response for after the user attempts to create a room.
        """

        pass


class StartRoomGameView(View):
    """
    View for a VIP player client forcefully (or otherwise) starting a game.

    Note that there is no server-side verification needed to start a game, just the correct session user must be the
    one to kick off the game.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Attempt to retrieve the game state of an already started game.

        This method would be used for each client

        The types of outcomes are:

        - Success: Game has already started, user has correct room code and username that already existed.
        - Failure: Game has started but the user is not recognised in the game by that username.
        - Failure: Game has not started yet.
        - Failure: Game does not exist.

        Parameters
        ----------
        request: `HttpRequest`
            The `HttpRequest`.

        Returns
        -------
        `HttpResponse`
            JSON response used to
        """

        pass

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Attempt to start a game and return a payload containing all the information pre-fed for the game.

        Parameters
        ----------
        request: `HttpRequest`
            The `HttpRequest`.

        Returns
        -------
        `HttpResponse`
            JSON response used to
        """

        pass
