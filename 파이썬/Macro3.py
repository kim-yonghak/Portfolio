import pyautogui
import keyboard
import time
import pydirectinput

count = 0
stop_flag = False
countValue = 10 # 몇회를 돌 것인지

pydirectinput.click(1700, 974, button = 'left')     
time.sleep(0.5)  
pydirectinput.click(962, 704, button = 'left') 
time.sleep(0.5)
pyautogui.hotkey('esc')
time.sleep(0.5)

while count != countValue and not stop_flag: # 1로 바꾸면 무한 사이클
    pydirectinput.click(962, 993, button = 'left')
    time.sleep(3)
    pyautogui.hotkey('F9')
    time.sleep(0.5)
    pydirectinput.click(1749, 827, button = 'left')
    time.sleep(0.5)
    pyautogui.hotkey('esc')
    time.sleep(0.5)
    count += 1

    if keyboard.is_pressed('q'): # 즉시 중단 키
        stop_flag = True
        
pydirectinput.click(962, 993, button = 'left')
time.sleep(3)
pyautogui.hotkey('F9')
