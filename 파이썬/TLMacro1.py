import pyautogui
from PIL import ImageGrab
import time
import pydirectinput
import keyboard

pydirectinput.FAILSAFE = False

def step1():
    print("step1")
    i = 1330100
    stop_flag = False
    color1 = (237, 93, 42)
    color2 = (253, 100, 46)
    while not stop_flag:
        #screenshot = ImageGrab.grab()  # 화면 캡처
        
        time.sleep(0.5)
        pydirectinput.click(43, 947, button = 'left')
        print(repr(i))
        pyautogui.write("@itemdelete")
        time.sleep(0.5)
        pyautogui.hotkey('Enter')
        time.sleep(0.5)
        pyautogui.write("@spawn " + repr(i) + " 1 100")
        time.sleep(0.5)
        pyautogui.hotkey('Enter')
        time.sleep(1)
        pyautogui.write("@killnpc")
        time.sleep(0.5)
        pyautogui.hotkey('Enter')

        step2(color1, color2)
        i += 1
        
        if i == 1330110:
            break

        if keyboard.is_pressed('q'): # 즉시 중단 키
            stop_flag = True
            
        time.sleep(0.5)  # 일정 간격으로 반복 체크

def step2(target_color1, target_color2):
    print("step2")
    stop_flag = False
    while not stop_flag:

        pydirectinput.click(1640, 785, button = 'left')
        screenshot = ImageGrab.grab() # 화면 캡처
        pixel_color1 = screenshot.getpixel((935, 175))
        pixel_color2 = screenshot.getpixel((1014, 179))     
        
        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            time.sleep(0.5)
            pydirectinput.click(1750, 40, button = 'left')
            time.sleep(1)
            pyautogui.hotkey('alt','f1')
            time.sleep(0.5)
            pydirectinput.click(1750, 40, button = 'left')
            time.sleep(1)
            pydirectinput.click(43, 947, button = 'left')
            break

        if keyboard.is_pressed('q'): # 즉시 중단 키
            stop_flag = True
            
        time.sleep(0.5)  # 일정 간격으로 반복 체크

if __name__ == "__main__":
    print("start")

    pydirectinput.click(990, 540, button = 'left')
    step1()
       
    print("done")
