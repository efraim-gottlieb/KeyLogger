import ctypes
def print_text(text):
    ctypes.windll.user32.MessageBoxW(0, text, "KeyLogger", 1)
