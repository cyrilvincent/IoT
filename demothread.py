import threading
import time

class DemoThread(threading.Thread):

    def __init__(self, mac, sleep):
        threading.Thread.__init__(self)
        self.mac = mac
        self.sleep = sleep
        self.sum = 0

    def run(self):
        for i in range(60):
            print(f"{self.mac}:{i}")
            time.sleep(self.sleep)
            self.sum += i

t1 = DemoThread("T1",0.5)
t2 = DemoThread("T2",2/3)
t3 = DemoThread("T3",0.1)
t4 = DemoThread("T4",1)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
print(t1.sum)
t2.join()
print(t2.sum)



