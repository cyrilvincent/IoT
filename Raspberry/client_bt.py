import bluetooth
import config

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
mac = config.mac
sock.connect((mac, 1))

def readline():
    s = ""
    while(True):
        data = sock.recv(1024).decode()
        s += data
        if '\r\n' in data:
            break
    return s

while(True):
    data = readline()
    print(data)