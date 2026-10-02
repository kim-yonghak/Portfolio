import pyautogui
from PIL import ImageGrab
import keyboard

def extract_cursor_pixel_color():
    while True:
        if keyboard.is_pressed('q'):  # Q 키가 눌리면 종료
            print("Exiting the program...")
            break

        if keyboard.is_pressed('enter'):  # 엔터 키가 눌리면
            x, y = pyautogui.position()  # 현재 마우스 커서 위치 얻기
            #x = 935
            #y = 175
            screenshot = ImageGrab.grab(bbox=(x, y, x+1, y+1))  # 해당 위치의 픽셀 캡처
            pixel_color = screenshot.getpixel((0, 0))  # 캡처한 픽셀의 색상 추출
            position = pyautogui.position()
            print("Cursor pixel:", position)
            print("Cursor pixel color:", pixel_color)

if __name__ == "__main__":
    print("Press Enter key to extract cursor pixel color. Press Q to exit.")
    extract_cursor_pixel_color()
