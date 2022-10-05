FROM python:3.10.5-slim-buster as base

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONFAULTHANDLER=1

RUN useradd --create-home appuser
USER appuser

RUN mkdir /home/appuser/app && \
    mkdir /home/appuser/appdeps
WORKDIR /home/appuser/app

FROM base as build

ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VERSION=1.2.1

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .
COPY LICENSE.txt .

RUN python3 -m poetry export --without dev -f requirements.txt -o requirements.txt && \
    pip install --target=/home/appuser/appdeps --force-reinstall -r requirements.txt

COPY entrypoint.sh .
COPY omnihost omnihost

FROM base

ENV OMNIHOST_SOURCE_DIR=null
ENV OMNIHOST_HTML_OUTPUT_DIR=null
ENV OMNIHOST_GEMINI_OUTPUT_DIR=null
ENV OMNIHOST_GOPHER_OUTPUT_DIR=null
ENV OMNIHOST_CSS_TEMPLATE_PATH=null

ENV PATH="/home/appuser/appdeps:$PATH"

COPY --from=build /home/appuser/app .
COPY --from=build /home/appuser/appdeps /home/appuser/appdeps

#ENTRYPOINT ["/bin/bash", "entrypoint.sh", "--"]
#CMD ["-h"]