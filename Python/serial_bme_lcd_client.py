import serial
import time
import serial.tools.list_ports

# ce script DOIT tourner en CLI

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)


port = "COM6"
print(f"Open serial on {port}")
sock = serial.Serial(port, baudrate=9600)
print(sock)

while True:
    s = input("Input> ")
    s = sock.write((s + "\n").encode())
    time.sleep(0.01)
    s = sock.readline()
    print(s.decode().strip())
    time.sleep(0.01)
    
sock.close()
