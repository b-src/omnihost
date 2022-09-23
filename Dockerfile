FROM python:3.10.5-slim-buster as base

WORKDIR /app

FROM base as build

RUN pip install poetry

COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .
COPY LICENSE.txt .

RUN python3 -m venv env && \
    . env/bin/activate && \
    poetry install --no-interaction --no-root --without dev

COPY omnihost omnihost

RUN poetry install --only-root

FROM base

ENV OMNIHOST_SOURCE_DIR=null
ENV OMNIHOST_HTML_OUTPUT_DIR=null
ENV OMNIHOST_GEMINI_OUTPUT_DIR=null
ENV OMNIHOST_GOPHER_OUTPUT_DIR=null
ENV OMNIHOST_CSS_TEMPLATE_PATH=null

COPY --from=build /app .