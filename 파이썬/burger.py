import pyautogui
import keyboard
import time
import pydirectinput

pydirectinput.click(1700, 900, button = 'left')

str1 = "test "
t = 1000
s = 1

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write(str1 + " " + str(t))
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Gold 9999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset Cash 9999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset BattlePoint 9999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset ArtifactPoint 9999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

time.sleep(0.2)
pyautogui.hotkey('`')
time.sleep(0.2)
pyautogui.write("SetAsset WonderCoin 9999999")
time.sleep(0.2)
pyautogui.hotkey('Enter')

