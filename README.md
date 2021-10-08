# pyhole-bot
A simple python project to update pi-hole-block-list project

## Requirements

- python >= 3.9.7
- pip wheel
- pyenv virtualenv
- Internet to update

## Running

Clone:

```sh
git clone https://github.com/thiago-scherrer/pyhole-bot
```

Enable virtualenv:

```sh

cd pyhole-bot
pyenv activate venv_pyhole_bot
```

Install requirements:

```sh
pip wheel -r requirements.txt
```

Export envs:

```sh

# blocklist output destination
export BLOCKLIST_OUTPUT='/path/output_blocklist.txt'

# blocklist endpoint providers
export URL_FILE='/path/endpoint_example.txt'
```

Run

```sh
python src/pyholebot/core.py
```
