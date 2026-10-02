import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def rune_auto(stop_flag, count):
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    while not stop_flag :
        if keyboard.is_pressed('q'): # 즉시 중단 키
            stop_flag = True

        pydirectinput.click(1680, 1015, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(0.1)

        pydirectinput.click(1100, 775, button = 'left')
        pydirectinput.mouseDown() 
        pydirectinput.mouseUp()
        time.sleep(3)

        count += 1

    return count
        



if __name__ == "__main__":
    print("룬 강화 시작(Q 입력 시 종료)")
    a = False
    b = 0
    b = rune_auto(a, b)
    print("강화 횟수 : ", b)

