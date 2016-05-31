def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg

def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("broken")
        totalsent = totalsent + sent
