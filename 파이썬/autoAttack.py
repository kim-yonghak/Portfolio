import pyautogui
from PIL import ImageGrab
import time
import pydirectinput

# 변화를 감지할 색상 RGB 값
target_color = (250, 96, 0)  # 상대 닉네임 색

def detect_color_change(target_color):
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
    detect_color_change(target_color)
