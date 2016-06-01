
import socket

import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
print "Server turn on. Listening port 2222..."
while True:
    conn, addr = s.accept()
    print 'Connection is established {}{}'.format(*addr)
    while True:
        data = conn.recv(1024)
        if b'close' in data:
            print 'Found "close" in data'
            conn.close()
        elif not data:
            print 'No data.'
            conn.close()
            break
        else:
            print 'Data received: ', data
            conn.send(data)
            conn.close()
