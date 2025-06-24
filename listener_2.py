from pynput import keyboard
from multiprocessing import Process
import time

from listener import on_release

input_keys = []

def run_listener():
    def on_press(key):
        global input_keys
        try:
            input_keys.append(key.char)
            print(input_keys)
        except:
            input_keys.append(str(key))
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def run_listener_forever():
    while True:
        p = Process(target=run_listener)
        p.start()
        p.join()
        p.terminate()


if __name__ == "__main__":
    run_listener_forever()
