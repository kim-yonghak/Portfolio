import pyautogui
import keyboard
import time
import pydirectinput

count = 0  # 몇회를 돌 것인지
stop_flag = False

while 1 : # count != 0 부분을 1로 바꾸면 무한 사이클
    while not stop_flag :
        pyautogui.hotkey('`')
        time.sleep(0.2)
        pyautogui.write("alone")
        time.sleep(0.2)
        pyautogui.hotkey('Enter')
        time.sleep(0.2)
        
        if keyboard.is_pressed('f'): # 즉시 중단 키
            stop_flag = True
    if keyboard.is_pressed('t'):
        stop_flag = False
