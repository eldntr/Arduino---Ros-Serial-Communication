import serial
import time

def test_serial():
    # Configure serial port
    ser = serial.Serial(
        port='/dev/ttyACM0',  # or ttyUSB0 depending on Arduino connection
        baudrate=9600,
        timeout=1
    )
    
    try:
        while True:
            # Send data
            message = "Hello Arduino!\n"
            ser.write(message.encode())
            print(f"Sent: {message}")
            
            # Read response
            if ser.in_waiting:
                response = ser.readline().decode().strip()
                print(f"Received: {response}")
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        ser.close()
        print("Serial port closed")

if __name__ == '__main__':
    test_serial()
