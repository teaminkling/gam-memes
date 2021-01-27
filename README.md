# Project "Memeforming"

> This application is unstable and not ready to be used.

A simple self-hosted/cloud meme creation game.

## About

Join or create a private lobby, enter a code, grab a bunch of meme templates, make them arty,
submit, and rate! This game is best experienced in Discord with friends.

## User Notes

### User-Submitted Content

This app relies on user-submitted content. We cannot ensure that the API backend we use for meme
templates will not  show NSFW or infringing content.

This is inevitable. The default API backend (Imgflip) is moderated and therefore the app should be
_relatively_ safe, but we won't take liability for getting banned if an infringing image shows
up on-stream.

### Security

There is minimal security in this app. Any room code can be joined (with very aggressive rate
limiting) with a valid username. Theoretically, a user can join on two different devices and
submit a meme submission twice.

The second submission will overwrite the first one. If an attacker joins a room by knowing the room
code and a username, it is possible to submit _any_ image as that user's submission.

## Development

The frontend shares data with the backend and helps build the state and 

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

This project runs using REST + HTTP. I don't believe there will be much of a performance overhead
for not using websockets. Long-polling and 30-second long promises can be made for pretty much
anything that requires a response from the server, and the rest of the requests have an 
immediate success/failure response pattern.

### Directory Structure

This is the directory structure as a whole.

```txt
.
├── api           [ Backend code as a full-fledged web API source.                ]
├── components    [ Vue frontend-only components.                                 ]
├── data          [ Data storage/definitions, "transpiled" from the backend code. ]
├── layouts       [ Vue frontend-only base layouts, styles, and scripts.          ]
├── pages         [ Routing definition containing all app pages in the frontend.  ]
├── static        [ Served static files (as-is) for the frontend.                 ]
├── store         [ Vue frontend store that manages state. Should not be touched. ]
├── types         [ Frontend TypeScript support files. Should not be touched.     ]
└── utils         [ Vue frontend utilities. Likely won't need to be touched.      ]
```

If I limit it to just important directories:

```txt
.
├── api           [ Backend code as a full-fledged web API source.                ]
├── components    [ Vue frontend-only components.                                 ]
├── layouts       [ Vue frontend-only base layouts, styles, and scripts.          ]
├── pages         [ Routing definition containing all app pages in the frontend.  ]
└── static        [ Served static files (as-is) for the frontend.                 ]
```

## TODO

- Adjust the allowed hosts.
- Rate limiting.
- Use of cache backend.
- Move constants/things that are shared between frontend/backend to their own system.
