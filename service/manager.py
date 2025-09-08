import threading
from time import sleep
from service.listener import Listener
from service.data_collector import Package
from networkwriter import NetworkWriter
from backend.server import app
import socket
hostname = socket.gethostname()

class Manager:
    def __init__(self, hours=5):
        self.listener = Listener()
        self.service = threading.Thread(target=self.listener.run)
        self.hours = hours
        self.run = False
        self.run_server = threading.Thread(
            target=app.run,
            kwargs={'host': '0.0.0.0', 'port': 5000, 'use_reloader': False},
            daemon=True
        )

    def start(self):
        self.service.start()
        self.run = True
        self.run_server.start()
        print('Listener and server is running !')
        while self.run:
            sleep(self.hours)
            temp_data = self.listener.get_keys()
            if temp_data:
                data = Package(temp_data)
                data = str(data.export_package())
                nw = NetworkWriter()
                nw.send_data({"machine": hostname,"data": data})
    def stop(self):
        self.listener.stop()
        self.run = False
if __name__ == '__main__':
    p = Manager()
    p.start()