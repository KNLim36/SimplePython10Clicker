import pyautogui
import win32api
import win32con
import time

def click(x, y, clicks=10):
    win32api.SetCursorPos((x, y))
    for i in range(clicks):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

while True:
    if win32api.GetAsyncKeyState(win32con.VK_RBUTTON):
        x, y = pyautogui.position()
        click(x, y, clicks=2)
        time.sleep(0.1)