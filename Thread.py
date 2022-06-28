# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import threading

class aThread(threading.Thread):
    def __init__(self, num, val):
        threading.Thread.__init__(self)
        self.threadNum=num
        self.loopCount=val
    
    def run(self):
        print("Starting run: ", self.threadNum)
        myfunc(self.threadNum, self.loopCount)
        

def myfunc(num, val):
    count=0
    while count< val:
        print(num, ":", val*count)
        count=count+1
    
t1=aThread(1,15)
t2=aThread(2,20)

t1.start()
t2.start()

threads=[]
threads.append(t1)
threads.append(t2)

for t in threads:
    t.join()
    




