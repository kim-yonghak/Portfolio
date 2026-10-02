import pyautogui
import keyboard
import time
import pydirectinput

pydirectinput.click(960, 950, button = 'left')
time.sleep(1)
pydirectinput.click(960, 900, button = 'left')
time.sleep(4)
pyautogui.keyDown('w')
time.sleep(3)
pyautogui.keyUp('w')
pyautogui.keyDown('f')
time.sleep(5)
pyautogui.keyUp('f')

pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Crystal 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Gold 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Cash 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset BattlePoint 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset ArtifactPoint 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset WonderCoin 999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.5)
pyautogui.hotkey('esc')
time.sleep(0.5)
pydirectinput.click(1120, 700, button = 'left')
