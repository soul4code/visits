# За базу используем официальный image питона
FROM python:3.9

# Отключаем буферизацию логов
ENV PYTHONUNBUFFERED 1

# Обновляем пакетный менеджер
RUN apt-get update -y && apt-get upgrade -y && apt-get install gunicorn libgeos-dev libgdal-dev -y

WORKDIR /app

ADD ./poetry.lock /app/poetry.lock
ADD ./pyproject.toml /app/pyproject.toml

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

RUN $HOME/.poetry/bin/poetry config virtualenvs.in-project true

RUN $HOME/.poetry/bin/poetry install

ADD . /app

WORKDIR /app
