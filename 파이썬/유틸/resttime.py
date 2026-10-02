import tkinter as tk
from datetime import timedelta
import time
import threading

# 항상 8시간으로 시작
countdown_time = timedelta(hours=8)

def format_time(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02}", f"{minutes:02}"

def update_display():
    h_str, m_str = format_time(countdown_time)
    hour_1.itemconfig("text", text=h_str[0])
    hour_2.itemconfig("text", text=h_str[1])
    min_1.itemconfig("text", text=m_str[0])
    min_2.itemconfig("text", text=m_str[1])

def countdown():
    global countdown_time
    while countdown_time.total_seconds() > 0:
        time.sleep(60)
        countdown_time -= timedelta(minutes=1)
        update_display()

def start_move(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def do_move(event):
    x = event.x_root - start_x
    y = event.y_root - start_y
    root.geometry(f"+{x}+{y}")

def close_on_escape(event):
    root.destroy()

# 숫자 박스 (Canvas + 그라데이션 배경 + 텍스트)
def create_rounded_digit(master, text="0"):
    width, height = 50, 50
    canvas = tk.Canvas(master, width=width, height=height, bg="#e4e4e4", highlightthickness=0)

    # 수직 그라데이션 채우기
    for i in range(height):
        # 위는 밝은 회색, 아래는 어두운 회색
        gray = 70 + int((40 / height) * i)  # 70~110 정도
        color = f"#{gray:02x}{gray:02x}{gray:02x}"
        canvas.create_line(5, i, width - 5, i, fill=color)

    # 텍스트만 위에 올림
    canvas.create_text(width // 2, height // 2, text=text, font=("Consolas", 30), fill="white", tags="text")
    return canvas

# GUI 시작
root = tk.Tk()
root.overrideredirect(True)
root.configure(bg="#7a7a7a")
root.attributes("-topmost", True)

start_x = 0
start_y = 0

main_frame = tk.Frame(root, bg="#e4e4e4", bd=0)
main_frame.pack(padx=3, pady=3)

# 타이틀
title = tk.Label(main_frame, text="잔여근무시간", font=("맑은 고딕", 18), bg="#e4e4e4", fg="#333333")
title.pack(pady=(6, 6))

time_frame = tk.Frame(main_frame, bg="#e4e4e4")
time_frame.pack(pady=(0, 8))

# 숫자 박스 및 콜론
hour_1 = create_rounded_digit(time_frame)
hour_2 = create_rounded_digit(time_frame)
colon = tk.Label(time_frame, text=":", font=("Segoe UI", 24), bg="#e4e4e4", fg="#3b4351")
min_1 = create_rounded_digit(time_frame)
min_2 = create_rounded_digit(time_frame)

# 간격 조정
hour_1.grid(row=0, column=0, padx=(0, 0))
hour_2.grid(row=0, column=1, padx=(0, 0))
colon.grid(row=0, column=2, padx=(0, 0))
min_1.grid(row=0, column=3, padx=(0, 0))
min_2.grid(row=0, column=4, padx=(0, 0))

# 드래그 이동
for widget in (root, main_frame, title, time_frame, hour_1, hour_2, min_1, min_2, colon):
    widget.bind("<Button-1>", start_move)
    widget.bind("<B1-Motion>", do_move)

# ESC 종료
root.bind("<Escape>", close_on_escape)

# 화면 중앙 배치
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.update_idletasks()
w = main_frame.winfo_reqwidth() + 6
h = main_frame.winfo_reqheight() + 6
x = (screen_width - w) // 2
y = (screen_height - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

# 실행
update_display()
threading.Thread(target=countdown, daemon=True).start()
root.mainloop()
