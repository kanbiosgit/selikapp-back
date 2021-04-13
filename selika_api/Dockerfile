FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update ; apt-get --assume-yes install binutils libproj-dev gdal-bin

RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/