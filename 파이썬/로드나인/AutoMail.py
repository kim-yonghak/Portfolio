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
    i = 0
    while i < 200:
        pydirectinput.click(1250, 1020, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.5)
        pydirectinput.click(940, 290, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.5)
        pydirectinput.click(960, 520, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        pyautogui.write("yhakk3PC")
        time.sleep(1)
        pydirectinput.click(960, 600, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.5)
        pydirectinput.click(825, 340, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        pyautogui.write("dd")
        time.sleep(0.6)
        pydirectinput.click(830, 420, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        pyautogui.write("dd")
        time.sleep(0.6)
        pydirectinput.click(1110, 860, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(4)
        i = i+1
