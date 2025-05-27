FROM ghcr.io/astral-sh/uv:python3.13-bookworm

RUN apt update && apt install --no-install-recommends -y curl

WORKDIR /app

COPY ./uv.lock ./pyproject.toml .

RUN uv sync --frozen
