import pickle
import socket

import netifaces as ni


class COM:
    def __init__(self, OPPip, txport, rxport):
        self.OPPip = OPPip
        self.txport = txport
        self.rxport = rxport
        self.tx = socket.socket()
        self.rx = socket.socket()
        self.ip = self.selfip()
        self.rx.bind((str(self.ip), int(rxport)))

    def stop(self):
        self.rx.close()
        self.tx.close()

    def send(self, msg):
        msg_b = pickle.dumps(msg)
        self.tx.send(msg_b)

    def recieve(self):
        msg_b = self.c.recv(1024)

        msg = pickle.loads(msg_b)
        return msg

    def listen(self):
        self.rx.listen()
        print("Listen accepted")

        self.c, self.addr = self.rx.accept()
        print(" socket accepted")

    def connect(self):
        self.tx.connect((str(self.OPPip), int(self.txport)))

    def selfip(self):
        ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
        return ip
