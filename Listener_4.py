from pynput import keyboard

class Listener:
    def __init__(self):
        self.data = []
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.atop_flag = False
    def on_press(self, key):
        try:
            char = key.char
        except:
            if key == keyboard.Key.space:
                char = " "
            elif key == keyboard.Key.enter:
                char = "\n"
        try:
            self.data.append(char)
        except:
            pass
        if self.atop_flag:
            return False

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()
    def stop(self):
        self.stop_flag = True
    def get_keys(self):
        text = "".join(self.data)
        self.data.clear()
        return text