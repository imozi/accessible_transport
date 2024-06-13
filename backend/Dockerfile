FROM python:3.11-alpine

RUN apk update && apk add --no-cache \
    curl \
    build-base \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    gcc \
    musl-dev \
    make

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY ./backend/pyproject.toml /app/

RUN poetry install --no-root

COPY ./backend /app/

RUN poetry update