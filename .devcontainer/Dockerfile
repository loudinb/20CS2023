FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl wget git \
    && wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.5.57/quarto-1.5.57-linux-amd64.deb \
    && apt-get install -y ./quarto-1.5.57-linux-amd64.deb

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Copy requirements.txt and install packages
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
