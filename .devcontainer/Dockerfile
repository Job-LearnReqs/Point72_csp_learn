FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        autoconf \
        autoconf-archive \
        automake \
        bison \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        flex \
        gdb \
        git \
        gnupg \
        libtool \
        make \
        ninja-build \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        tar \
        unzip \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key \
        | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_22.x nodistro main" \
        > /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
    && npm install -g @openai/codex@latest \
    && npm cache clean --force \
    && rm -rf /var/lib/apt/lists/*
