import pyautogui
import keyboard
import time
import pydirectinput
import tkinter as tk
from tkinter import simpledialog, Label, messagebox

count = 0
stop_flag = False

# tkinter를 이용하여 값을 입력받는 커스텀 다이얼로그 생성
root = tk.Tk()
root.withdraw()  # 창을 표시하지 않음

dialog = tk.Toplevel(root)
dialog.title("원더러스 유물 뽑기 매크로")
dialog.geometry("350x150")

label = Label(dialog, text="유물 뽑기 메인 화면에서 실행해 주세요.\n매크로 중단 키 : Q", padx=10, pady=10, wraplength=350)
label.pack()

countValue = simpledialog.askinteger("입력", "몇회를 돌 것인지 입력하세요 (0 = 무한):", parent=dialog, minvalue=0)

# 사용자가 Cancel 버튼을 눌렀을 경우 코드 실행을 중단
if countValue is None:
    exit()

pydirectinput.click(1700, 975, button='left')
time.sleep(0.5)
pydirectinput.click(1160, 750, button='left')
time.sleep(0.5)
pyautogui.hotkey('esc')
time.sleep(0.5)

if countValue == 0:
    while not stop_flag:  # 무한 루프
        pydirectinput.click(962, 993, button='left')
        time.sleep(3)
        pyautogui.hotkey('F9')
        time.sleep(0.5)
        pydirectinput.click(1749, 827, button='left')
        time.sleep(0.5)
        pyautogui.hotkey('esc')
        time.sleep(0.5)

        if keyboard.is_pressed('q'):
            stop_flag = True
else:
    while count < countValue - 1 and not stop_flag:
        pydirectinput.click(962, 993, button='left')
        time.sleep(3)
        pyautogui.hotkey('F9')
        time.sleep(0.5)
        pydirectinput.click(1749, 827, button='left')
        time.sleep(0.5)
        pyautogui.hotkey('esc')
        time.sleep(0.5)
        count += 1

        if keyboard.is_pressed('q'):
            stop_flag = True

pydirectinput.click(962, 993, button='left')
time.sleep(3)
pyautogui.hotkey('F9')


# 작업이 완료되었음을 알리는 메시지 창
messagebox.showinfo("완료", "매크로 실행이 완료되었습니다.")
