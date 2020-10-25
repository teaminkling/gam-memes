# sup

yo this repo sucks (except the neat template we made) but the code is fine, gonna just poop out my code and fix this
up later.

public repo? we're professionals, trust me :)

## note if you found this randomly

this game is not ready for twitch or any livestreaming app. not because it sucks but because it relies on user content.
this means we cannot guarantee that images provided are SFW.

there is a review process in place to implement this and other streamer-friendly services in the future.

## points that need to be added to docs later

- admin provided by django is a fallback: we will implement our own admin views
- security is not a primary concern but privacy is; we do not record data of users or even users at all, but this means
  it is fairly easy to "spoof" a user. caution is given to the user when this happens.
- data mining strategy: every week (or arbitrary period of time) the server will data mine new popular memes from the
  source api. but this isn't going to give us a lot of variety. we should also

## features that are dope

> but these features aren't there yet

- meme rating and reviewing: some meme templates aren't that good, so we want to rate each one as we see it.
- robust game management/disconnect management: seamless disconnect and reconnect even across devices (repeated server
  calls simply favour the latest call for the user). not that secure, but who cares honestly.
- being able to see all of the meme templates in a game before the game is even created (room creator only).
- 1st place, 2nd place, 3rd place votes for games with 3+ players.

## devs beware

- run everything with DEBUG=1 prefixing the manage command. either do that or prefix it with a SECRET_KEY.

## why not websocket

mostly because i want to iterate quickly and i don't believe there will be much of a performance overhead. we can use
long-polling and 30-second long promises for pretty much anything that requires a response from the server, and the
rest of the requests have an immediate success/failure response pattern.

## tests

look, we love tests and tdd/bdd but we all know it does add a dev performance overhead. let's just not do them and then
improve quality so we can move fast, break things, and make our friends happy that we have such a great app?

tests will be implemented later.

## todo

lots of todo items but these ones aren't in code comments:

- adjust the allowed hosts.
- rate limiting and other neat security features.
- use of cache backend.
- run collectstatic
- associate the player with the user's current session (this is how requests are made)
  - anonymous session: when a user is created it is permanently attached to the session which
    does not clear for a browser until the timeout or it is manually cleared.
      - this should work for ios too.

## constants

modify your constants in frontend/constants

## requests

as few requests as possible: that's the motto. the game creation POST should create the VIP user
for the game, create the game with the settings, and return a player list with the VIP user present.
the GET request should return the names and the details for each player, not their IDs.

in general, no IDs should be found in any serializer call: always the pure data.

GET requests to the game endpoint should therefore provide the requested fields so it doesn't show
the meme templates every time. this will help with bandwidth a bit.
