import serial
import time
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)

port = "COM6"
print(f"Open serial on {port}")
sock = serial.Serial(port, baudrate=9600)
print(sock)
while True:
    s = sock.readline()
    print(s.decode().strip())
    time.sleep(0.01)
    
sock.close()
