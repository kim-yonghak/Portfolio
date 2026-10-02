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
        pydirectinput.click(1650, 870, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
        pydirectinput.click(1080, 920, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.2)
