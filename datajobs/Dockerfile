# Pull official base image
FROM python:3.8-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
# From: https://github.com/Hudrolax/uc-docker/blob/master/Dockerfile
RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    fluxbox \
    wget \
    unzip \
    gnupg \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install xterm
RUN apt-get update && apt-get install -y xterm

# Install Google Chrome from .deb (it's works only on x86 docker host machine, not ARM or Apple Silicon)
RUN apt-get update && apt-get install -y wget gnupg2 apt-utils --no-install-recommends \
    && wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || true \
    && apt-get install -fy \
    && rm -rf /var/lib/apt/lists/* google-chrome-stable_current_amd64.deb \
    && which google-chrome-stable || (echo 'Google Chrome was not installed' && exit 1)

# Install x11vnc
RUN mkdir ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd

# Set work directory
WORKDIR /usr/src/datajobs

# Install project dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# Test browser webdriver
# COPY ./test.py .
# RUN python3 -m test

# Copy project
COPY . .
