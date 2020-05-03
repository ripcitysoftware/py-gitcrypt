FROM python:3.8.2-alpine3.11
MAINTAINER chris.maki@ripcitysoftware.com

# Create working directory
RUN mkdir /project
WORKDIR /project
RUN apk add git git-crypt make zip rsync gcc libc-dev libffi-dev py-cryptography openssl-dev --update && \
    pip install pipenv
