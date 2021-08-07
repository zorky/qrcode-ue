FROM python:3.8.6-slim-buster
RUN apt-get clean
RUN apt-get update
RUN mkdir /code && mkdir /static
RUN apt-get clean
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /code

