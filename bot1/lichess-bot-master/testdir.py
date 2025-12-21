
import time
import socket

SOCK = "/tmp/binary.sock"
class Random:
    def get_bit(self):
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(SOCK)
        bit = s.recv(1).decode()
        s.close()
        return bit

    def start(self):
        print("inside the start function")
        bit = self.get_bit()
        print(bit)

r = Random()
r.start()
