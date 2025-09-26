import threading
import http.client
import time
import json

class HelloHTTPRead(threading.Thread):
    
    def __init__(self, id, sleep, url, callback):
        super().__init__()
        self.id = id
        self.sleep = sleep
        self.callback = callback
        self.connection = http.client.HTTPConnection(url)
        
    def run(self):
        while True:
            self.connection.request("GET", "/")
            r1 = self.connection.getresponse()
            data = r1.read().decode()
            print(data)
            self.callback(self.id, "hello", data)
            time.sleep(self.sleep)

class TempHTTPRead(threading.Thread):
    
    def __init__(self, id, sleep, url, callback):
        super().__init__()
        self.id = id
        self.sleep = sleep
        self.callback = callback
        self.connection = http.client.HTTPConnection(url)
        
    def run(self):
        while True:
            self.connection.request("GET", "/all")
            r1 = self.connection.getresponse()
            data = r1.read().decode()
            data = json.loads(data)
            self.callback(self.id, "temp", data["temp"])
            time.sleep(self.sleep)
            
class HumidityHTTPRead(threading.Thread):
    
    def __init__(self, id, sleep, url, callback):
        super().__init__()
        self.id = id
        self.sleep = sleep
        self.callback = callback
        self.connection = http.client.HTTPConnection(url)
        
    def run(self):
        while True:
            self.connection.request("GET", "/all")
            r1 = self.connection.getresponse()
            data = r1.read().decode()
            data = json.loads(data)
            self.callback(self.id, "hum", data["hum"])
            time.sleep(self.sleep)
            
class PressureHTTPRead(threading.Thread):
    
    def __init__(self, id, sleep, url, callback):
        super().__init__()
        self.id = id
        self.sleep = sleep
        self.callback = callback
        self.connection = http.client.HTTPConnection(url)
        
    def run(self):
        while True:
            self.connection.request("GET", "/all")
            r1 = self.connection.getresponse()
            data = r1.read().decode()
            data = json.loads(data)
            self.callback(self.id, "pre", data["pre"])
            time.sleep(self.sleep)
            
class DisplayHTTPWrite(threading.Thread):
    
    def __init__(self, id, sleep, url, callback):
        super().__init__()
        self.id = id
        self.sleep = sleep
        self.callback = callback
        self.connection = http.client.HTTPConnection(url)
        
    def run(self):
        i = 0
        while True:
            self.connection.request("GET", f"/display/Hello_{i}")
            i+=1
            r1 = self.connection.getresponse()
            data = r1.read().decode()
            time.sleep(self.sleep)    
        
        

class MainService:
    
    def __init__(self, url):
        self.url = url
        
    def start(self):
        print("Starting")
        
        # temp = TempHTTPRead(0, 1, self.url, self.callback)
        # temp.start()
        # humidity = HumidityHTTPRead(1, 2, self.url, self.callback)
        # humidity.start()
        # pressure = PressureHTTPRead(2, 4, self.url, self.callback)
        # pressure.start()
        # display = DisplayHTTPWrite(3, 1, self.url, None)
        # display.start()
        hello1  = HelloHTTPRead(0, 1, self.url, self.callback)
        hello1.start()
        hello2  = HelloHTTPRead(1, 2, self.url, self.callback)
        hello2.start()
        hello3  = HelloHTTPRead(2, 3, self.url, self.callback)
        hello3.start()
               
    def callback(self, sender, sensor, value):
        if type(value) == str:
            print(f"Received from thread {sender}: {value}")
        else:
            print(f"Received from thread {sender}: {sensor}={value:.2f}")
       

if __name__ == "__main__":
    # service = MainService("192.168.1.210:5000")
    service = MainService("192.168.1.59:5000")
    service.start()
    
        
        
        
        