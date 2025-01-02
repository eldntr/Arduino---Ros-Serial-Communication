To run, do:

1. `sudo ./setup.sh`
2. `docker exec arduino_container arduino-cli compile --fqbn arduino:avr:uno serial_test`
3. `docker exec arduino_container arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno serial_test`
4. `docker exec -it ros2_container python3 /ros2_ws/serial_test.py`

Ensure your computer have installed docker and docker-compose