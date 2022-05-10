FROM python:3.10-alpine

ENV APP_USER=app_user \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.13

# Create and setup workdir
RUN mkdir -p /srv/
WORKDIR /srv

RUN apk add --no-cache \
        gcc \
        libffi-dev \
        libxslt-dev \
        musl-dev \
        python3-dev \
        zlib-dev \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        git \
        libxml2-dev \
        linux-headers \
        xmlsec-dev

RUN pip install "poetry==$POETRY_VERSION"

COPY poetry.lock pyproject.toml /srv/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY app.py /srv/

CMD poetry run python app.py
