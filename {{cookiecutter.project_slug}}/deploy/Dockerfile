FROM python:3.8-slim as base

ENV C_FORCE_ROOT=true \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # prometheus
    prometheus_multiproc_dir=/var/run/prometheus \
    # poetry:
    POETRY_VERSION=1.1.4 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt update \
    && apt-get install -y gcc \
                      binutils \
                      gettext \
                      nginx \
                      make \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${POETRY_VERSION}/get-poetry.py | python \
    && poetry install --no-dev --no-ansi \
    && apt-get remove --purge -y gcc binutils \
    && apt-get autoremove -y

# ---

FROM base as production

COPY . .

RUN export DJANGO_ENV=build \
    && python manage.py collectstatic --noinput --verbosity 0 \
    && django-admin compilemessages \
    && cp deploy/nginx/* /etc/nginx

ENV DJANGO_ENV=production

CMD ["/bin/bash", "deploy/server/backend.sh"]

# ---

FROM base as test

RUN poetry install --no-ansi

COPY . .
