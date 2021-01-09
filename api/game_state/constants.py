"""
Constants used for the game state.

Notes
-----
If they are grouped up, they should all start with the same prefix and all states with that prefix
should ideally start with a different character. If this is not possible, they should at least
start with a different word.
"""

from typing import Collection, Tuple, Set

#
# Game state constants.
#

GAME_STATE_CREATING: int = 1
GAME_STATE_CREATING_DESCRIPTION: str = "Creating Game Room"
"""The game is being configured by the host user."""

GAME_STATE_WAITING_FOR_PLAYERS: int = 2
GAME_STATE_WAITING_FOR_PLAYERS_DESCRIPTION: str = "Waiting for Players"
"""The game is waiting for the room host user to start."""

GAME_STATE_FORGING_MEMES: int = 3
GAME_STATE_FORGING_MEMES_DESCRIPTION: str = "Forging Memes"
"""Players are now creating memes under a time limit."""

GAME_STATE_JUDGING_MEMES: int = 4
GAME_STATE_JUDGING_MEMES_DESCRIPTION: str = "Judging Memes"
"""Players are adding their votes to their preferred meme."""

GAME_STATE_PRESENTING_WINNERS: int = 5
GAME_STATE_PRESENTING_WINNERS_DESCRIPTION: str = "Presenting Winners"
"""The game is showing a presentation of the memes."""

GAME_STATES: Collection[Tuple[int, str]] = (
    (GAME_STATE_CREATING, GAME_STATE_CREATING_DESCRIPTION),
    (GAME_STATE_WAITING_FOR_PLAYERS, GAME_STATE_WAITING_FOR_PLAYERS_DESCRIPTION),
    (GAME_STATE_FORGING_MEMES, GAME_STATE_FORGING_MEMES_DESCRIPTION),
    (GAME_STATE_JUDGING_MEMES, GAME_STATE_JUDGING_MEMES_DESCRIPTION),
    (GAME_STATE_PRESENTING_WINNERS, GAME_STATE_PRESENTING_WINNERS_DESCRIPTION),
)
"""All the states a game can choose from."""

#
# Game room.
#

GAME_ROOM_CODE_LENGTH: int = 4
"""The length of the game code."""

TOTAL_CODE_REGEN_ATTEMPTS: int = 100
"""Number of attempts the system will make at most to regenerate the room code on collision."""

#
# Word lists.
#

# noinspection SpellCheckingInspection
PROHIBITED_ROOM_CODE_WORDS: Set[str] = {
    "ANUS",
    "ARSE",
    "BTCH",
    "BICH",
    "CLIT",
    "CLTS",
    "COCK",
    "COCC",
    "COKK",
    "COKC",
    "COON",
    "CUNT",
    "DAGO",
    "DAMN",
    "DICK",
    "DIKE",
    "DYKE",
    "FAGT",
    "FAGG",
    "FAGA",
    "FAGO",
    "FAGU",
    "FAGI",
    "FARK",
    "FUCC",
    "FUCK",
    "FUKT",
    "FUCT",
    "GOOK",
    "GOUK",
    "HEEB",
    "HOMO",
    "JAPS",
    "JAPP",
    "JIZZ",
    "JIZM",
    "JISM",
    "KIKE",
    "KYKE",
    "KYKK",
    "MICK",
    "MICC",
    "MUFF",
    "NIGR",
    "NIGA",
    "PAKI",
    "PAKK",
    "PISS",
    "POON",
    "PUTO",
    "SHIT",
    "SHYT",
    "SHTY",
    "SHTT",
    "SLUT",
    "SLTY",
    "SMEG",
    "TARD",
    "TITS",
    "TWAT",
    "WANK",
}
"""
Words that should not show up on streams or may offend players of the game.

Notes
-----
Well, this isn't going to look good on the public code search.

In all seriousness, Inkling Interactive is committed to ensuring a safe and friendly environment 
for as many people as possible while playing our games or using our work. If you would like to 
contribute to this list (especially if an offensive word has been seen in-game), please feel free
to contact us or open a pull request.
"""
