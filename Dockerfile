FROM python:2.7.14-stretch

RUN apt-get update

RUN apt-get install -y yui-compressor libclosure-compiler-java sass

RUN pip install google-api-python-client==1.2 Cactus==3.3.3

WORKDIR /app

ADD . /app

RUN cactus build

