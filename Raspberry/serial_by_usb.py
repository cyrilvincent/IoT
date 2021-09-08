import serial
import config

sock = serial.Serial(config.usb)
s = sock.readline()
print(s.decode().strip())
for i in range(10):
    msg = "TOTO" + str(i) +"\n"
    sock.write(msg.encode())
    s = sock.readline()
    print(s.decode().strip())
sock.close()
