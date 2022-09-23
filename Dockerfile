FROM python:3.10.5-slim-buster as base

WORKDIR /app

FROM base as build

RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

RUN python3 -m venv env && \
    . env/bin/activate && \
    poetry install --no-interaction --no-root --without dev

COPY omnihost omnihost

RUN poetry install --only-root

FROM base

COPY --from=build /app .