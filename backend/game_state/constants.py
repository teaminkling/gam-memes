"""
Constants used for the game state.

Notes
-----
If they are grouped up, they should all start with the same prefix and all states with that prefix should ideally start
with a different character. If this is not possible, they should at least start with a different word.

An example of this is `GAME_STATE_CREATING` and `GAME_STATE_CREATING_MEMES`. The latter was changed to
`GAME_STATE_FORGING_MEMES` and it still makes sense but now starts with an F.
"""

from typing import Collection, Tuple

#
# Game state constants.
#

GAME_STATE_CREATING: str = "Creating Game Room"
"""The game is being configured by the host user."""

GAME_STATE_WAITING_FOR_PLAYERS: str = "Waiting for Players"
"""The game is waiting for the room host user to start."""

GAME_STATE_FORGING_MEMES: str = "Forging Memes"
"""Players are now creating memes under a time limit."""

GAME_STATE_JUDGING_MEMES: str = "Judging Memes"
"""Players are adding their votes to their preferred meme."""

GAME_STATE_PRESENTING_WINNERS: str = "Presenting Winners"
"""The game is showing a presentation of the memes."""

GAME_STATES: Collection[Tuple[str, str]] = (
    (GAME_STATE_CREATING, GAME_STATE_CREATING),
    (GAME_STATE_WAITING_FOR_PLAYERS, GAME_STATE_WAITING_FOR_PLAYERS),
    (GAME_STATE_FORGING_MEMES, GAME_STATE_FORGING_MEMES),
    (GAME_STATE_JUDGING_MEMES, GAME_STATE_JUDGING_MEMES),
    (GAME_STATE_PRESENTING_WINNERS, GAME_STATE_PRESENTING_WINNERS),
)
"""All the states a game can choose from."""

#
# Game room.
#

GAME_ROOM_CODE_LENGTH: int = 4
"""The length of the game code."""
