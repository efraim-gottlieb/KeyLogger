from pynput import keyboard
from multiprocessing import Process
import time

list = []

def listener_func():
    def on_press(key):
        list.append(key)
        print(list)
        return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def run_listener_forever():
    while True:
        p = Process(target=listener_func)
        p.start()
        p.join()
        p.terminate()


if __name__ == "__main__":
    run_listener_forever()
