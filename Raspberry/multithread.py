import threading
import time

class MyThread(threading.Thread):

    def __init__(self, number, sleep):
        threading.Thread.__init__(self);
        self.number = number
        self.sleep = sleep

    def run(self):
        for i in range(100):
            print("Message from number " + str(self.number) + ": " + str(i))
            time.sleep(self.sleep)

if __name__ == '__main__':
    thread1 = MyThread(number=1, sleep=1)
    thread1.start()
    thread2 = MyThread(number=2, sleep=2 + 1 / 3)
    thread2.start()
    thread3 = MyThread(number=3, sleep=0.43333)
    thread3.start()