FROM python:3.11-slim

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN pip3 install poetry && curl -sSL 'https://install.python-poetry.org' | python3 - 

ENV PYTHONPATH="$PYTHONPATH:/app"

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--without dev") --no-interaction --no-ansi

COPY . .