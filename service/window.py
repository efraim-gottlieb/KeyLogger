import ctypes
import time
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

# פונקציות
GetForegroundWindow = user32.GetForegroundWindow
GetForegroundWindow.restype = wintypes.HWND

GetWindowTextLengthW = user32.GetWindowTextLengthW
GetWindowTextLengthW.argtypes = [wintypes.HWND]
GetWindowTextLengthW.restype = ctypes.c_int

GetWindowTextW = user32.GetWindowTextW
GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
GetWindowTextW.restype = ctypes.c_int

def get_active_window_title():
    hwnd = GetForegroundWindow()
    length = GetWindowTextLengthW(hwnd) + 1
    buffer = ctypes.create_unicode_buffer(length)
    GetWindowTextW(hwnd, buffer, length)
    return buffer.value