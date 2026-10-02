import time
import pyautogui

# 실행 후 대상 창으로 이동할 시간
print("3초 후 매크로가 시작됩니다.")
print("중지하려면 마우스를 화면 왼쪽 위 모서리로 이동하세요.")
time.sleep(3)

# 각 키 입력 사이의 기본 대기 시간
pyautogui.PAUSE = 0.1

try:
    while True:
        # 위쪽 방향키
        pyautogui.press("up")
        time.sleep(0.1)

        # Ctrl + Shift + 위쪽 방향키
        pyautogui.hotkey("ctrl", "shift", "up")
        time.sleep(0.1)

        # F4
        pyautogui.press("f4")
        time.sleep(0.3)

except pyautogui.FailSafeException:
    print("매크로가 중지되었습니다.")
