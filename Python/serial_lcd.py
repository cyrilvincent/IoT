import serial
import config

print(f"Open serial on {config.usb}")
sock = serial.Serial(config.usb)
print(sock)
for i in range(10):
    msg = "TOTO" + str(i) +"\n"
    sock.write(msg.encode())
sock.close()
