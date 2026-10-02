import pyautogui
import keyboard
import time
import pydirectinput

count = 0 # 몇회를 돌 것인지
stop_flag = False

pydirectinput.click(1700, 974, button = 'left')     
time.sleep(0.5)  
pydirectinput.click(962, 704, button = 'left') 
time.sleep(9)

while count != 10 and not stop_flag: # count != 0 부분을 1로 바꾸면 무한 사이클
    pydirectinput.click(962, 993, button = 'left') 
    time.sleep(2)   
    pydirectinput.click(1749, 827, button = 'left')
    time.sleep(9)
    count += 1

    if keyboard.is_pressed('q'): # 즉시 중단 키
        stop_flag = True
        
pydirectinput.click(962, 993, button = 'left') 
