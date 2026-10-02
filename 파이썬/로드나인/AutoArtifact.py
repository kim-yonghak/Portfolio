import pyautogui
import keyboard
import time
import pydirectinput
import keyboard

if __name__ == "__main__":
    print("뽑기 시작")
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    while 1:
        pydirectinput.click(1760, 930, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.1)
        pydirectinput.click(1835, 35, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.6)
