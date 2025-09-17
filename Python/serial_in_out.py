import serial
import config

port = "COM6"
print(f"Open serial on {port}")
sock = serial.Serial(port, baudrate=9600)
while True:
    msg = input("Order: ")
    msg += "\n"
    sock.write(msg.encode())
    s = sock.readline()
    print(s.decode().strip())
sock.close()
