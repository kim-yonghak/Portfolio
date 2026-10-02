import pyautogui
import keyboard
import time
import pydirectinput
import keyboard

if __name__ == "__main__":
    print("확정 시작")
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    while 1:
        pydirectinput.click(470, 920, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
        pydirectinput.click(1660, 400, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
        pydirectinput.click(1000, 920, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
        pydirectinput.click(740, 1020, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
        pydirectinput.click(1800, 1025, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.5)
        pydirectinput.click(970, 1000, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
