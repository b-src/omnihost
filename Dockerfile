FROM python:3.10.5-slim-buster as base

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONFAULTHANDLER=1

RUN useradd --create-home appuser
USER appuser

RUN mkdir /home/appuser/app \
    /home/appuser/source \
    /home/appuser/stylesheet_source \
    /home/appuser/html_output \
    /home/appuser/gemini_output \
    /home/appuser/gopher_output

WORKDIR /home/appuser/app

FROM base as build

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_VERSION=1.2.1

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock README.md LICENSE.txt ./

RUN python3 -m poetry export --without dev -f requirements.txt -o requirements.txt


FROM base

ENV OMNIHOST_SOURCE_DIR=null \
    OMNIHOST_HTML_OUTPUT_DIR=null \
    OMNIHOST_GEMINI_OUTPUT_DIR=null \
    OMNIHOST_GOPHER_OUTPUT_DIR=null \
    OMNIHOST_CSS_TEMPLATE_PATH=null

COPY --from=build /home/appuser/app/requirements.txt .

RUN pip install --force-reinstall -r requirements.txt

COPY entrypoint.sh .
COPY omnihost omnihost

ENTRYPOINT ["/bin/bash", "entrypoint.sh"]