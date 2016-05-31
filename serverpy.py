# primitive server utility on python
import socket
from correctrwsocket import myreceive, mysend

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
print "Server turn on. Listening localhost:1234"
while True:
    conn, addr = s.accept()
    while True:
        try:
            data = myreceive(conn, 1024)
        except Exception as err:
            print err
            data = None
        if not data:
            break
        else:
            print '''Client with {addr} is connected. Received: 
{data}'''.format(addr=addr, data=data)
	try:
            mysend(conn, data)
        except Exception as er:
            print er
    conn.close()
