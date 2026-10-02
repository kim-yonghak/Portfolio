import pyautogui
import keyboard
import time
import pydirectinput

pydirectinput.click(1700, 900, button = 'left')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Crystal 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Gold 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Cash 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset BattlePoint 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset ArtifactPoint 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset WonderCoin 500")
time.sleep(0.2)
pyautogui.hotkey('Enter')

