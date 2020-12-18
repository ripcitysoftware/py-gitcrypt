FROM python:3.8.2-buster
MAINTAINER chris.maki@ripcitysoftware.com

# Create working directory
RUN mkdir /project
WORKDIR /project
RUN apt-get update && \
    apt-get install git-crypt zip rsync && \
    pip install --upgrade pip && \
    pip install pipenv && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/root/.poetry/bin:$PATH"
