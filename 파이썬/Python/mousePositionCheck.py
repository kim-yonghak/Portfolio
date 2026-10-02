import pyautogui
import keyboard
import time

while 1:
    position = pyautogui.position()
    if keyboard.is_pressed('enter'):
        print(position)
        time.sleep(0.2)
