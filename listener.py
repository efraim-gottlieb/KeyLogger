from pynput import keyboard
import time
from print_text import *
input_keys = []
start_time = time.localtime()[4]
def on_press(key):
    try:
        if (time.localtime()[4]+1) == start_time:
            input_keys.append()
        input_keys.append(key.char)
    except:
        input_keys.append(str(key))

###     stop monitoring     ###
def on_release(key):
    try:
        show = input_keys[-1] == 'w' and input_keys[-2] == 'o' and input_keys[-3] == 'h' and input_keys[-4] == 's'
        if show:
        ###     enter 'show' to view the last memory keys       ###
            input_keys.pop()
            input_keys.pop()
            input_keys.pop()
            input_keys.pop()
            output_text = "".join(input_keys)
            print_text(output_text)

        ###     press "c + delete" to stop monitoring       ###
        elif key == keyboard.Key.delete and input_keys[-2] == 'c':
                return False
    except:
        pass

###     keyboard listener      ###
def run_listener():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


run_listener()

