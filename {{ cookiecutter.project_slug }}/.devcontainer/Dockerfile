FROM python:${PYTHON_VERSION}-slim

WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install uv

COPY . .

RUN uv install
