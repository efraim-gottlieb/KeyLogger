from log_creator import create_log

def encryptor(data):
    return str((data[::-1]))

def send_to_server(data):
    if data:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f'{create_log(data)}\n')