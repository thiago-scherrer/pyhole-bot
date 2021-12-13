# pyhole-bot
A simple python project to update pi-hole-block-list project

## requirements

- docker >= 20.10.9
- docker-compose >= 2.0.1

## running

Clone:

```sh
git clone https://github.com/thiago-scherrer/pyhole-bot
```

Build:

```sh
cd pyhole-bot
docker-compose build
```

Configure:

Change `URL_FILE` and `BLOCKLIST_OUTPUT` in `docker-compose.yml` where:

- URL_FILE: block list library. You can leave the default to use the current list for this project
- BLOCKLIST_OUTPUT: where will save the generated list

Run:

```sh
docker-compose run
```

Blocklist output on `/tmp/blocklist.txt`


### using the list

Go to `Adlist` and add a new list locally like this:

```sh
file:///tmp/gravity.list
```
