# pyhole-bot
A simple python project to update pi-hole-block-list project

## Requirements

- docker >= 20.10.9
- docker-compose >= 2.0.1

## Running

Clone:

```sh
git clone https://github.com/thiago-scherrer/pyhole-bot
```

Build:

```sh
cd pyhole-bot
docker-compose build
```

Run:

```sh
docker-compose run
```

Blocklist output on `/tmp/blocklist.txt`
