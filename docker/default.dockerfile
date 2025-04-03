ARG PYTHON_VERSION=3.10

FROM public.ecr.aws/docker/library/python:${PYTHON_VERSION}-slim as poetry_builder

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/opt/poetry"

# hadolint ignore=DL4006,DL3008
RUN apt-get update \
    && apt-get install --no-install-recommends --assume-yes curl \
    && rm -rf /var/lib/apt/lists/*
# hadolint ignore=DL4006
RUN curl -sSL https://install.python-poetry.org | python3 -

FROM public.ecr.aws/docker/library/python:${PYTHON_VERSION}-slim as builder

ENV PATH="/opt/poetry/bin:$PATH"
ENV POETRY_VIRTUALENVS_IN_PROJECT=0
ENV POETRY_VIRTUALENVS_CREATE=0
ENV POETRY_CACHE_DIR="/tmp/poetry_cache"

ARG PROJECT_PATH

WORKDIR /opt/project

COPY --from=poetry_builder "/opt/poetry" "/opt/poetry"
COPY ./$PROJECT_PATH/pyproject.toml $PROJECT_PATH/
COPY ./$PROJECT_PATH/poetry.lock $PROJECT_PATH/
COPY packages packages

# hadolint ignore=DL3003
RUN cd $PROJECT_PATH && poetry install --only dev,main --no-root --no-directory
# hadolint ignore=DL3003
RUN cd $PROJECT_PATH && poetry install --only dev,main

FROM public.ecr.aws/docker/library/python:${PYTHON_VERSION}-slim as runner

ARG PROJECT_PATH

WORKDIR /opt/project

COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /usr/local/bin /usr/local/bin
COPY packages /opt/project/packages

CMD ["sh", "-c", "cd $PROJECT_PATH && ./scripts/entrypoint.sh"]
