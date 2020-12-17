FROM python:3.8.2-alpine3.11
MAINTAINER chris.maki@ripcitysoftware.com

# Create working directory
RUN mkdir /project
WORKDIR /project
RUN apk add git curl git-crypt make zip rsync gcc libc-dev libffi-dev py-cryptography openssl-dev g++ --update && \
    pip install --upgrade pip && \
    pip install pipenv && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/root/.poetry/bin:$PATH"