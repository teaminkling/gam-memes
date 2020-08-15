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

- meme rating and reviewing: some meme templates aren't that good, so we want to rate each one as we see it.
- robust game management/disconnect management: seamless disconnect and reconnect even across devices (repeated server
  calls simply favour the latest call for the user). not that secure, but who cares honestly.
- being able to see all of the meme templates in a game before the game is even created (room creator only).
