# memeware.io

> This application is unstable and not ready to be used.

A simple self-hosted/cloud meme creation game.

## About

Join or create a private lobby, enter a code, grab a bunch of meme templates, make them funny,  submit, and rate!
This game is best experienced in Discord with friends.

- Staff review process for boring, NSFW, infringing, or unfunny memes.
- Secure guest (single device) or logged-in user support.
- A robust backend for multiple different frontends.
- A beautiful and unique default web frontend.
- Open source with a permissive license for those who really don't like ads.
- App-level rate limiting in conjunction with network-layer rate limiting.
- REST and HTTP-based API for simplicity (not Websockets).
- Support for `memcached` as a cache backend.
- Optimised for PostgreSQL.

## Development

Build and run the frontend as a dev server:

```sh
npm install
npm run dev
```

Build the Django backend (assuming knowledge of `pyenv` and `pipenv`):

> Every `manage.py` command must start with `DEBUG=1` (not recommended) or supply a `SECRET_KEY` (recommended).

```sh
pyenv install 3.8.8  # Or a later patch version. Later minor/major versions may also work.
pipenv install       # Only need to do this once per dependency change.
pipenv shell
```

Run the server:

```sh
SECRET_KEY=<something> python manage.py collectstatic
SECRET_KEY=<something> python manage.py migrate
SECRET_KEY=<something> python manage.py runserver 8000
```

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

### Notes

Note that the frontends and backends are heavily separate from each other (for now); each change made to the backend 
should be communicated to the frontend as well.

This is a monorepo with all Inkling Interactive frontends created in the same place.
