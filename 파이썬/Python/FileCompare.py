#정지기능 추가
import pyautogui
import keyboard
import time

pyautogui.click(x=115,y=1060, interval=0.1)
time.sleep(0.5)
pyautogui.write("WinMerge")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
    
pyautogui.click(x=23,y=33, interval=0.1)
time.sleep(0.5)
pyautogui.click(x=55,y=97, interval=0.1)
time.sleep(0.5)
pyautogui.click(x=395,y=432, interval=0.1)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("D:\\OlderFile") #예전 데이터 파일 폴더
time.sleep(0.5)
pyautogui.click(x=395,y=507, interval=0.1)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write("D:\\NewFile") #신규 데이터 파일 폴더
time.sleep(0.5)
pyautogui.click(x=1552,y=730, interval=0.1)
time.sleep(5) #폴더 비교 시간
pyautogui.click(x=265,y=28, interval=0.1)
time.sleep(0.5)
pyautogui.click(x=302,y=125, interval=0.1)
time.sleep(0.5)
pyautogui.click(x=1039,y=591, interval=0.1)
time.sleep(0.5)
pyautogui.click(x=1080,y=575, interval=0.1)
