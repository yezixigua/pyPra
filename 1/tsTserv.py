# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 19:43:54 2018

@author: an
"""
from socket import *
from time import ctime

HOST = ''
Port = 21567
BUFSIZ = 1024
ADDR = (HOST,Port)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('wait for connection ....')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connect from:')
    print(addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' %(ctime() , data), encoding= 'utf-8'))
        
    tcpCliSock.close()
tcpSerSock.close()

