from threading import Thread
import time


class Hello(Thread):
    def run(self):
        for i in range(20):
            print("hello")
            time.sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(20):
            print("Hi")
            time.sleep(1)


a = Hello()
b = Hi()
a.start()
time.sleep(0.2)
b.start()
a.join()
b.join()
print("Bye")
