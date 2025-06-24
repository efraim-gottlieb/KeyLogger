import ctypes
def msgbox(text):
    ctypes.windll.user32.MessageBoxW(0, text, "KeyLogger", 1)
