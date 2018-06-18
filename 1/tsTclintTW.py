# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:46:01 2018

@author: an
"""

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 20567

class TSClntprotocol(protocol.Protocol):
    def sendData(self):
        data = input('> ')
        if data:
            print('sending data: ' % data)
            self.transparent.write(data)
        else:
            self.transparent.lossConnection()
            
    def connectionMade(self):
        self.sendData()
        
    def dataReceived(self, data):
        print(data)
        self.sendData()
        
class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntprotocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()
    
reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()