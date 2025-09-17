import serial
import config

port = "COM6"
print(f"Open serial on {port}")
sock = serial.Serial(port, baudrate=9600)
print(sock)
for i in range(10):
    msg = "TOTO" + str(i) +"\n"
    sock.write(msg.encode())
sock.close()
