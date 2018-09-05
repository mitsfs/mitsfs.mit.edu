FROM python:2.7.14-stretch AS build

RUN apt-get update \
  && apt-get install -y yui-compressor closure-compiler sass

RUN pip install google-api-python-client==1.2 Cactus==3.3.3

WORKDIR /app

COPY . /app

RUN cactus build -c production.json

FROM resin/raspberrypi3-alpine:3.7

COPY --from build /app/.build/ /mitsfs

RUN setup-xorg-base

RUN apk -update --no-cache add
  xf86-video-fbdev \
  xf86-video-vesa \
  xf86-input-mouse \
  xf86-input-keyboard \
  dbus ​\
  set​xkbmap \
  kbd \
  rc-update ​\
  ​add \
  dbus \
  xfce \
  chromium

COPY door-schedule /usr/bin/

CMD startx


