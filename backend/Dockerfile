FROM ghcr.io/astral-sh/uv:python3.13-bookworm

RUN apt update && apt install --no-install-recommends -y curl

WORKDIR /app

COPY ./backend/uv.lock ./backend/pyproject.toml .

RUN uv sync --frozen

COPY ./envs/backend.env /opt/.env
COPY ./backend .

ENTRYPOINT ["fastapi", "run", "--root-path=/api"]
