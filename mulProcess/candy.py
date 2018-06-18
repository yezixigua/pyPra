# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:25:09 2018

@author: an
"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print('Refilling candy.....')
    try:
        candytray.release()
    except ValueError:
        print('full, skipping')
    else:
        print('OK')
        
    lock.release()
    
def buy():
    lock.acquire()
    print('Buying candy...')
    if candytray.acquire(False):
        print('ok')
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))
    
def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))
        
def _main():
    print('starting at :', ctime())
    nloops = randrange(2, 6)
    print('The candy machine (Full with %d bars)!' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print('All done at:', ctime())

if __name__ == '__main__':
    _main()    
    
    









