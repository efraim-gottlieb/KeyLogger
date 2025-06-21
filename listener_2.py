from pynput import keyboard
from multiprocessing import Process
import time

input_keys = []

def listener_func():
    def on_press(key):
        global input_keys
        input_keys.append(key)
        printt()
        print(key)
        # מסיים את המאזין מיידית
        return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def run_listener_forever():
    while True:
        p = Process(target=listener_func)
        p.start()
        p.join()  # מחכה לסיום ההאזנה הנוכחית
        p.terminate()  # לוודא שהוא מת

def printt():
    print(input_keys)
# התחלת האזנה בלולאה
if __name__ == "__main__":
    run_listener_forever()
