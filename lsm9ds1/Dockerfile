ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apt-get update && \
    apt-get install -y python3 python3-pip i2c-tools && \
    pip3 install adafruit-circuitpython-lsm9ds1 paho-mqtt

COPY run.sh /run.sh
COPY tilt.py /tilt.py
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
