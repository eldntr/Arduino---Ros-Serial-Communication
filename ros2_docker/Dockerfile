FROM osrf/ros:foxy-desktop

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install pyserial && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws
