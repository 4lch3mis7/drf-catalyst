FROM alpine:latest

# Do not write byte code
ENV PYTHONDONTWRITEBYTECODE=1
# Do not buffer stdout and stderr
ENV PYTHONUNBUFFERED=1

# Install dev tools
RUN apk update && apk add --no-cache \
    build-base \
    linux-headers \
    bash \
    python3 \
    python3-dev \
    py3-pip \
    py3-gunicorn \
    py3-uv

# Install tzdata for timezone support
RUN apk add --no-cache tzdata

WORKDIR /app

# Copy requirements
COPY pyproject.toml uv.lock ./

# Install packages only needed for building, install and clean on a single layer
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && uv v && source .venv/bin/activate && uv pip install pycurl \
    && apk del .build-dependencies && uv sync --frozen

# Copy project
COPY . /app

# Expose port
EXPOSE 8000

ENTRYPOINT ["bash", "/app/entrypoint.sh"]
