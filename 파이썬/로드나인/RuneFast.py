import pyautogui
pyautogui.PAUSE = 0.05

if __name__ == "__main__":
    print("뽑기 시작")
    pyautogui.mouseDown(960, 570)
    pyautogui.mouseUp(960, 570)
    pyautogui.mouseDown(960, 570)
    pyautogui.mouseUp(960, 570)
    
    pos1 = (260, 260)
    pos2 = (1635, 1010)

    while True:
        pyautogui.mouseDown(*pos1)
        pyautogui.mouseUp(*pos1)
        pyautogui.mouseDown(*pos2)
        pyautogui.mouseUp(*pos2)
