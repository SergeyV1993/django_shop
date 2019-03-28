FROM python:3
RUN mkdir /shop
WORKDIR /shop
ADD requirements.txt /shop
RUN pip install -r requirements.txt
ADD . /shop


