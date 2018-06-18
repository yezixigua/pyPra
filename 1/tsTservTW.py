# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:30:00 2018

@author: an
"""

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from :', clnt)
        
    def dataReceived(self, data):
        self.transport.write('[%s] , %S' % (ctime(), data))
        
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connetion')
reactor.listenTCP(PORT, factory)
reactor.run()


