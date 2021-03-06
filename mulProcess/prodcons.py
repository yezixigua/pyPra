# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 16:05:37 2018

@author: an
"""

from random import randint
from time import sleep
from queue import Queue
from MyThread import MyThread

def writeQ(Queue):
    print('producing object for Q...')
    Queue.put('xxx', 1)
    print('size now', Queue.qsize())
    
def readQ(Queue):
    val = Queue.get(1)
    print('consumed object from Q ...size now', Queue.qsize())
    
def writer(Queue, loops):
    for i in range(loops):
        writeQ(Queue)
        sleep(randint(1, 3))
        
def reader(Queue, loops):
    for i in range(loops):
        readQ(Queue)
        sleep(randint(1, 3))
        
funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = Queue(32)
    
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    
    for i in nfuncs:
        threads[i].start()
    
    for i in nfuncs:
        threads[i].join()
        
    print('All done')
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    