import pyautogui
import keyboard
import time
import pydirectinput
import os
from PIL import Image

count = 0
stop_flag = False
countValue = 10 # 몇회를 돌 것인지

directory = 'C:\STOVE\playwonder\Arena\Saved\Screenshots\WindowsClient' # 스크린샷 경로
directory2 = 'D:\Yhakk\Result' # 저장 경로

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
time.sleep(3)

for filename in os.listdir(directory): # 스크린샷 편집
    if filename.endswith('.jpg') or filename.endswith('.png'):
        
        image = Image.open(os.path.join(directory, filename))

        roi1 = image.crop((282, 482, 400, 598)) # 편집 위치 및 크기
        roi2 = image.crop((593, 482, 711, 598))
        roi3 = image.crop((901, 482, 1019, 598))
        roi4 = image.crop((1207, 482, 1325, 598))
        roi5 = image.crop((1517, 482, 1635, 598))

        os.remove(os.path.join(directory, filename))

        roi1.save(os.path.join(directory2, 'roi1_' + filename))
        roi2.save(os.path.join(directory2, 'roi2_' + filename))
        roi3.save(os.path.join(directory2, 'roi3_' + filename))
        roi4.save(os.path.join(directory2, 'roi4_' + filename))
        roi5.save(os.path.join(directory2, 'roi5_' + filename))

