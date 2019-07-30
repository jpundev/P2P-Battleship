import socket, pickle

def transmit(address, port, msg):
    tx = socket.socket()
    tx.connect((str(address), port))
    msg_b = pickle.loads(msg)
    tx.send(msg_b)
    tx.close()

def recieve(address, port):
    rx= socket.socket()
    rx.bind((str(address), port))
    rx.listen(5)
    c, addr = rx.accept()
    msg_b = c.recv(1024)
    msg = pickle.dumps(msg_b)
    print(msg)