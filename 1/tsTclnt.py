# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 21:43:06 2018

@author: an
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    data = bytes(data,encoding='utf-8')
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)
    
tcpCliSock.close()
    