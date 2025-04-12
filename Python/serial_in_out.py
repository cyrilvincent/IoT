import serial
import config

print(f"Open serial on {config.usb}")
sock = serial.Serial(config.usb)
while True:
    msg = input("Order: ")
    msg += "\n"
    sock.write(msg.encode())
    s = sock.readline()
    print(s.decode().strip())
sock.close()
