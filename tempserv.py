
import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
print "Server turn on. Listening port 2222..."
count = 0# 
childs = []#
while True:
    conn, addr = s.accept()
    try:#
        count += 1#
        pid = os.fork()#
    except:#
        print 'error: create child'#
        count -= 1#
        os._exit(1)#
    if pid == 0:#
        print 'child: ', os.getpid()#
        print 'Connection is established {}:{}'.format(*addr)
        while True:
            data = conn.recv(1024)
            if b'close' in data:
                print 'Found "close" in data'
                conn.close()
                break
            elif not data:
                print 'No data.'
                conn.close()
                break
            else:
                print 'Data received: ', data
                conn.send(data)
        os._exit(0)#
    if pid > 0:#
        print 'parent: ', os.getpid()#
        childs.append(pid)#
        conn.close()
for p in childs:#
    pid, status = os.wait()#
    print 'pid {} - status= {}'.format(pid,
os.WEXITSTATUS(status))#
