FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y curl unzip git && \
    rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

RUN arduino-cli config init && \
    arduino-cli core update-index && \
    arduino-cli core install arduino:avr

ENV PATH="/root/.arduinoide/bin:${PATH}"

WORKDIR /arduino_ws

CMD ["arduino-cli", "daemon"]
