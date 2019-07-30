import socket, pickle

class COM:
    def __init__(self, OPPip, txport, rxport):
        self.tx = socket.socket()
        self.tx.connect((str(OPPip), txport))
        self.rx = socket.socket()
        self.rx.bind((str(OPPip), rxport))

    def stop(self):
        self.rx.close()
        self.tx.close()

    def send(self,msg):
        msg_b = pickle.loads(msg)
        self.tx.send(msg_b)

    def recieve(self):


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