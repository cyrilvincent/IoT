import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
mac = "00:0E:EA:CF:47:5A"
sock.connect((mac, 1))

def readline():
    s = ""
    while(True):
        data = bluetooth.recv(1024).decode()
        s += data
        if '\r\n' in data:
            break;
    return s

while(True):
    data = readline()
    print(data)