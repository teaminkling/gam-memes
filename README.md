# Memeforming

> This application is unstable and not ready to be used.

A dead simple self-hosted/cloud meme creation game.

## About

Join or create a private lobby, enter a code, grab a bunch of meme templates, make them arty, submit, and rate! This
game is best experienced in Discord or some voice call with a few drinks.

## Notes

### User-Submitted Content

This app relies on user-submitted content. We cannot ensure that the API backend we use for meme templates will not
show NSFW or infringing content.

This is inevitable. The default API backend (Imgflip) is moderated and therefore the app should be _relatively_ safe
but we won't take liability for getting banned if an infringing image shows up on stream.

### Security

There is minimal security in this app. Any room code can be joined (with very aggressive rate limiting) with a valid
username. Theoretically, a user can join on two different devices and submit a meme submission twice.

The second submission will overwrite the first one. If an attacker joins a room by knowing the room code and a
username, it is possible to submit _any_ image as that user's submission.

## Development

Build and run the frontend as a dev server:

```sh
npm install
npm run dev
```

Run the Django backend also as a dev server:

> Every `manage.py` command must start with `DEBUG=1` or supply an explicit `SECRET_KEY`.

```sh
pipenv install
pipenv shell
DEBUG=1 python manage.py collectstatic
DEBUG=1 python manage.py migrate
DEBUG=1 python manage.py runserver 8000
```

### Request/Response and not Websockets

This project runs using REST + HTTP. I don't believe there will be much of a performance overhead for not using
websockets. Long-polling and 30-second long promises can be made for pretty much anything that requires a response
from the server and the rest of the requests have an immediate success/failure response pattern.

### constants

Modify your constants in frontend/constants.

## TODO

There are a lot of TODO items, unfortunately:

- Adjust the allowed hosts.
- Rate limiting.
- Use of cache backend.
- Move constants/things that are shared between frontend/backend to their own system.
