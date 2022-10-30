FROM debian:11
FROM python:3.10.6-slim-buster
FROM nikolaik/python-nodejs:python3.9-nodejs18

WORKDIR /Aztech/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get -y install git
RUN apt-get install libxml2-dev libxslt-dev python

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "Aztech"]
