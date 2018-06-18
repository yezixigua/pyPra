# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:23:44 2018

@author: an
"""

import MyThread
from time import ctime, sleep

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return (fib(x-2) + fib(x - 1))

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return (x * fac(x - 1))

def sumVal(x):
    sleep(0.1)
    if x < 2: return 1
    return (x + sumVal(x - 1))

funcs = [fib, fac, sumVal]
n = 12

def main():
    nfuncs = range(len(funcs))
    
    print('*** single thread')
    for i in nfuncs:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())
        
    print('\n *** multiple threads')
    
    threads = []
    
    for i in nfuncs:
        t = MyThread.MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
        
    for i in nfuncs:
        threads[i].start()
        
    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
        
    print('All done')
    
if __name__ == '__main__':
    main()














