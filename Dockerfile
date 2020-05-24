FROM python:latest
RUN mkdir /shop
WORKDIR /shop
RUN pip install --upgrade pip
ADD requirements.txt /shop
RUN pip install -r requirements.txt
ADD . /shop


