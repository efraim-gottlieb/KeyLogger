from suspicious_text_checker import SuspiciousTextChecker
from time_stamp import time_stamp
from pc_info import get_system_info

class Package:
    def __init__(self, data):
        self.time_stamp = time_stamp()
        self.data = data
        # Check if Suspicious
        data_info = SuspiciousTextChecker(text=str(self.data),file_path="suspicious_words.txt")
        self.label = data_info.is_suspicious()
        self.suspicious_words = data_info.find_suspicious()
        self.pc_info = get_system_info()

    def export_package(self):
        return {
            "computer name":self.pc_info['computer_name'],
            "country" : self.pc_info['location']['country'],
            "city" : self.pc_info['location']['city'],
            "time" : self.time_stamp,
            "label" : self.label,
            "suspicious words" : self.suspicious_words,
            "data" : self.data
        }
if __name__ == '__main__':

    d = {'fr':'hack', 'moi':'hack'}
    a = Package(data=d)
    print(a.export_package()['data'])
    print(a.export_package())