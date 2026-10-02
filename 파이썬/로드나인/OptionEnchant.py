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
    cnt = 0
    x = 1275
    y = 200
    h = 1
    while cnt < 20:
        time.sleep(0.5)
        pydirectinput.click(x, y, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        i = 0
        while i < h:
            pydirectinput.click(1500, 510, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(1135, 665, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(1085, 740, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(765, 880, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(1100, 680, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(765, 880, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.click(765, 880, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(1.75)
            pydirectinput.click(940,905, button = 'left')
            pydirectinput.mouseDown() 
            pydirectinput.mouseUp()
            time.sleep(0.5)
            i += 1
        cnt += 1
        h += 1
        if x == 1500:
            x = 1275
            y += 75
        else:
            x += 75
        pydirectinput.click(495,400, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.5)
        pydirectinput.click(495,400, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
