FROM python:3.8.12-slim

RUN apt-get update

ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin::/home/.local/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install poetry

COPY . /home/appuser
WORKDIR /home/appuser/
RUN poetry install
