FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl wget git \
    && ARCH=$(dpkg --print-architecture) \
    && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.57/quarto-1.5.57-linux-$ARCH.deb \
    && apt-get install -y ./quarto-1.5.57-linux-$ARCH.deb \
    && rm ./quarto-1.5.57-linux-$ARCH.deb \
    && apt-get install -y graphviz \
    && apt-get install -y default-jre \
    && apt-get install -y plantuml \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements.txt and install packages
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

ENV GRAPHVIZ_DOT=/usr/bin/dot