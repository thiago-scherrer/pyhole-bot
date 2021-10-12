FROM python:3

RUN useradd pyhole-bot \
    && mkdir /home/pyhole-bot/.local \
    && chown pyhole-bot. /home/pyhole-bot -R

USER pyhole-bot

WORKDIR /home/pyhole-bot

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "src/pyholebot/core.py" ]
