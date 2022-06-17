# pyhole-bot

[![test](https://github.com/thiago-scherrer/pyhole-bot/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/thiago-scherrer/pyhole-bot/actions/workflows/test.yml)

A simple python project to update pihole block list

# requirements

- docker or podman
- docker-compose or podman-compose

## running

Build:

```sh
$ git clone https://github.com/thiago-scherrer/pyhole-bot

$ cd pyhole-bot

$ docker-compose build
```

Configure:

Change `URL_FILE` and `BLOCKLIST_OUTPUT` in `docker-compose.yml` where:

- `URL_FILE`: block list library. You can leave the default to use the current list for this project
- `BLOCKLIST_OUTPUT`: where will save the generated list

Run:

```sh
docker-compose run
```

Blocklist output on `/tmp/blocklist.txt`

