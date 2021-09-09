import serial
import config

# 2 cartes Arduino

sock1 = serial.Serial(config.usb)
sock2 = serial.Serial(config.usb2)
for i in range(1000):
    data1 = sock1.readline()
    data2 = sock2.readline()
    print(data1)
    print(data2)
sock1.close()
sock2.close()
