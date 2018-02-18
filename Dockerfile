FROM python:2.7.14-stretch

RUN apt-get update

RUN apt-get install -y yui-compressor closure-compiler sass

RUN ln -s /usr/bin/yui-compressor /usr/bin/yuicompressor

RUN pip install google-api-python-client==1.2 Cactus==3.3.3

WORKDIR /app

ADD . /app

EXPOSE 8000

CMD ["cactus", "serve"]
