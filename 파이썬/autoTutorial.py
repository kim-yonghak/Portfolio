import pyautogui
from PIL import ImageGrab
import time
import pydirectinput

pydirectinput.FAILSAFE = False

color1 = (255, 255, 255)
color2 = (0, 0, 0)

def step1(target_color1, target_color2):
    print("step1")
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처
        
        pixel_color1 = screenshot.getpixel((950, 311))
        pixel_color2 = screenshot.getpixel((86, 982))
        
        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            time.sleep(0.3)
            pydirectinput.moveTo(950, 450)
            pydirectinput.click()
            pydirectinput.click()
            pydirectinput.click()
            break
            
        time.sleep(0.5)  # 일정 간격으로 반복 체크

def step2(target_color1, target_color2):
    print("step2")
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처

        pixel_color1 = screenshot.getpixel((830, 133))
        pixel_color2 = screenshot.getpixel((932, 941))

        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            pydirectinput.moveTo(659, 803)
            pydirectinput.click()
            break

        time.sleep(0.5)

def step3(target_color1, target_color2):
    print("step3")
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처

        pixel_color1 = screenshot.getpixel((388, 708))
        pixel_color2 = screenshot.getpixel((866, 816))

        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            time.sleep(1)
            pydirectinput.click()
            time.sleep(2)
            pydirectinput.click()
            time.sleep(6)
            pydirectinput.click()
            pydirectinput.keyDown('d')
            break

        time.sleep(0.5)

def step4(target_color1, target_color2):
    print("step4")
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처

        pixel_color1 = screenshot.getpixel((1457, 311))
        pixel_color2 = screenshot.getpixel((1844, 777))

        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            time.sleep(0.2)
            pydirectinput.press('space')
            pydirectinput.press('space')
            time.sleep(0.14)
            pydirectinput.press('space')
            pydirectinput.press('space')
            time.sleep(0.14)
            pydirectinput.press('space')
            pydirectinput.press('space')
            time.sleep(0.14)
            pydirectinput.press('space')
            pydirectinput.press('space')
            time.sleep(0.14)
            pydirectinput.press('space')
            pydirectinput.press('space')
            time.sleep(0.14)
            pydirectinput.press('space')
            pydirectinput.press('space')
            pydirectinput.keyUp('d')
            break

        time.sleep(0.5)

def step5(target_color1, target_color2):
    print("step5")
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처

        pixel_color1 = screenshot.getpixel((84, 363))
        pixel_color2 = screenshot.getpixel((96, 464))

        if pixel_color1 == target_color1 and pixel_color2 == target_color2:
            time.sleep(0.2)
            pydirectinput.moveTo(79, 676)
            pydirectinput.click()
            time.sleep(0.5)
            pydirectinput.moveTo(654,643)
            pydirectinput.click()
            time.sleep(0.5)
            pydirectinput.keyDown('d')
            time.sleep(2)
            pydirectinput.keyUp('d')
            time.sleep(4)
            pydirectinput.moveTo(1030, 540)
            time.sleep(1)
            pydirectinput.mouseDown()
            time.sleep(7)
            pydirectinput.mouseUp()
            time.sleep(0.5)
            pydirectinput.keyDown('w')
            time.sleep(0.9)
            pydirectinput.keyUp('w')
            pydirectinput.keyDown('d')
            time.sleep(1)
            pydirectinput.keyUp('d')
            pydirectinput.keyDown('s')
            time.sleep(1.7)
            pydirectinput.keyUp('s')
            pydirectinput.keyDown('a')
            time.sleep(1.5)
            pydirectinput.keyUp('a')
            pydirectinput.keyDown('w')
            time.sleep(1.7)
            pydirectinput.keyUp('w')
            time.sleep(5)
            pydirectinput.moveTo(1745, 330)
            pydirectinput.click()
            break

        time.sleep(0.5)

def auto_attack(target_color):
    while True:
        screenshot = ImageGrab.grab()  # 화면 캡처
        for x in range(screenshot.width):
            for y in range(screenshot.height):
                pixel_color = screenshot.getpixel((x, y))
                if pixel_color == target_color:
                    # 특정 색상을 발견하면 원하는 동작을 수행하도록 설정
                    pydirectinput.moveTo(x+50, y+100)
                    pydirectinput.mouseDown()
                    time.sleep(1.5)
                    pydirectinput.mouseUp()
                    break
            else:
                continue
            break
        time.sleep(0.5)  # 일정 간격으로 반복 체크
                    
        
if __name__ == "__main__":
    color1 = (165, 206, 255)
    color2 = (0, 0, 0)
    step1(color1, color2)
    
    color1 = (46, 99, 132)  
    color2 = (237, 242, 250)
    step2(color1, color2)

    color1 = (52, 86, 123)  
    color2 = (44, 56, 73)
    step3(color1, color2)

    color1 = (183, 148, 128)  
    color2 = (255, 255, 255)
    step4(color1, color2)
    
    color1 = (9, 11, 30)  
    color2 = (27, 24, 3)
    step5(color1, color2)

    color1 = (250, 96, 0)
    auto_attack(color1)
    
    print("done")
