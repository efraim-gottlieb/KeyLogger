from log_creator import create_log
from service.advanced_encryptor import Encrypt

def encryptor(data):
    return str((data[::-1]))

def send_to_server(data):
    if data:
        data = create_log(data)
        print(data)
        a = Encrypt()
        a.encrypt_text(data)
        b = a.encrypted
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f'{b}\n')

