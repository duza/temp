# primitive client utility on python

import socket
from correctrwsocket import mysend, myreceive

req = 'Hello, my dear friend, socket!'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Start connecting...'
s.connect(('127.0.0.1', 1234))
print 'Connection is established'
try:
    mysend(s, req)
    rsp = myreceive(s, 1024)
except Exception as err:
    print err
s.close()
