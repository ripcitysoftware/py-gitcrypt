FROM python:3.8.2-buster
MAINTAINER chris.maki@ripcitysoftware.com

# Create working directory
RUN apt-get update && \
    apt-get install git-crypt zip rsync --yes && \
    pip install --upgrade pip && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/root/.poetry/bin:$PATH"


# setup cm-toolkit
RUN mkdir -p /opt/cloudmanager/commands 
COPY pyproject.toml /opt/cloudmanager
WORKDIR /opt/cloudmanager
RUN poetry install
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

COPY cm-toolkit.py /bin/cm-toolkit
COPY commands* /opt/cloudmanager/commands

RUN mkdir /project
WORKDIR /project
