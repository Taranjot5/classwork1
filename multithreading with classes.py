from threading import *
from threading import Thread
class A(Thread):
    def f1 run(self):
        for x in range(5):
            print(x)
ob=A()
ob.start()
t1.thread(target=ob.start())
