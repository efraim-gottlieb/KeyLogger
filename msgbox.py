import ctypes
def msgbox(title,text):
    ctypes.windll.user32.MessageBoxW(0, text, title, 0)
