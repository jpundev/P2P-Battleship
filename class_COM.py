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
        c, addr = self.rx.accept()
        msg_b = c.recv(1024)
        msg = pickle.dumps(msg_b)
        return msg
