FROM python:3

RUN useradd pyhole-bot && rm -rfv /home/pyhole-bot/.local

USER pyhole-bot

WORKDIR /home/pyhole-bot

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "src/pyholebot/core.py" ]
