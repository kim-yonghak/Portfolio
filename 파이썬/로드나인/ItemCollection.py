import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def collection_item_setting():
    strt = input("순서를 선택해주세요(1, 2, 3): ")
    t = int(strt)

    a = """112220101
112220101
110120101
111020101
112020101
113120101
112120101
112220102
110120102
111020102
112020102
113120102
112120102
112220103
110120103
111020103
112020103
113120103
112120103
112220101
112220102
112220103
112220104
112230104
112240104
112230101
110130101
111030101
112030101
113130101
112130101
112230101
110130101
111030101
112030101
113130101
112130101
112230101
110130101
111030101
112030101
113130101
112130101
112230102
110130102
111030102
112030102
113130102
112130102
112230102
110130102
111030102
112030102
113130102
112130102
112230103
110130103
111030103
112030103
113130103
112130103
112230103
110130103
111030103
112030103
113130103
112130103
112230101
112230102
112230103
112240101
112240101
110140101
110140101
112240101
110140101
111040101
112040101
113140101
112140101
112240102
112240102
110140102
110140102
112240102
110140102
111040102
112040102
113140102
112140102
112240103
112240103
110140103
110140103
112240103
110140103
111040103
112040103
113140103
112140103
112240104
112240104
110140104
110140104
112240104
110140104
111040104
112040104
113140104
112140104
112240105
112240105
110140105
110140105
112240105
110140105
111040105
112040105
113140105
112140105
112240106
112240106
110140106
110140106
112240106
110140106
111040106
112040106
113140106
112140106
112240107
112240107
110140107
110140107
112240107
112240107
110140107
110140107
112240108
112240108
110140108
110140108
112240108
112240108
110140108
110140108
112240109
112240109
110140109
110140109
112240109
112240109
110140109
110140109
112240110
112240110
110140110
110140110
112240110
112240110
110140110
110140110
112240101
112240102
112240103
112240104
112240105
112240106
112240107
112240108
112240109
112240110
112240101
112240102
112240103
112240104
112240105
112240106
112240107
112240108
112240109
112240110
112240101
112240102
112240103
112240104
112240105
112240106
112240107
112240108
112240109
112240110
112250101
112240107
112250101
112250101
112250102
112240108
112250102
112250102
112250103
112240109
112250103
112250103
112250104
112240110
112250104
112250104
112250101
112250102
112250103
112250104
112255201
112255201
110155201
111055201
112055201
112155201
113155201
112255201
110155201
111055201
112055201
112155201
113155201
112255202
110155202
111055202
112055201
112155202
113155202
112255202
110155202
111055202
112055201
112155202
113155202
"""
    
    b = """0
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
7
7
7
7
7
7
9
9
9
9
9
9
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
12
9
9
9
7
7
7
7
9
9
9
9
9
9
7
7
7
7
9
9
9
9
9
9
7
7
7
7
9
9
9
9
9
9
7
7
7
7
9
9
9
9
9
9
7
7
7
7
9
9
9
9
9
9
7
7
7
7
9
9
9
9
9
9
9
9
9
9
12
12
12
12
9
9
9
9
12
12
12
12
9
9
9
9
12
12
12
12
9
9
9
9
12
12
12
12
7
7
7
7
7
7
7
7
7
7
9
9
9
9
9
9
9
9
9
9
12
12
12
12
12
12
12
12
12
12
8
9
9
9
8
9
9
9
8
9
9
9
8
9
9
9
12
12
12
12
9
9
9
9
9
9
9
12
12
12
12
12
12
9
9
9
9
9
9
12
12
12
12
12
12
"""
    
    ID1 = ",".join(a.split("\n"))
    Enc1 = ",".join(b.split("\n"))

    data = { "ID": ID1.split(","),
             "Enc" : list(map(int, filter(None, Enc1.split(","))))
             }


    index = 0  # 초기 인덱스
    total_length = len(data["ID"])
    half_index = total_length // 2

    first_index = 420
    second_index = 700

    time.sleep(3)  # 실행 후 3초 대기 (입력 창 활성화를 위해)

    id_value = 0
    enc_value = 0

    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)

    if t == 1:
        while index < first_index:
            id_value = data["ID"][index]  # 현재 ID 값
            enc_value = data["Enc"][index]  # 현재 Enc 값
            pyautogui.PAUSE = 0


            if enc_value == 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item {id_value} 1", interval=0)  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                
            else :
                # 띄어쓰기 포함한 입력
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@itemEnchant {id_value} 1 {enc_value}", interval=0)  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터

            index += 1  # 인덱스 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

    if t == 2:
        index = first_index
        while index < second_index:
            id_value = data["ID"][index]  # 현재 ID 값
            enc_value = data["Enc"][index]  # 현재 Enc 값

            if enc_value == 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item {id_value} 1")  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                
            else :
                # 띄어쓰기 포함한 입력
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@itemEnchant {id_value} 1 {enc_value}")  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터

            index += 1  # 인덱스 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

    if t == 3:
        index = second_index
        while index < total_length:
            id_value = data["ID"][index]  # 현재 ID 값
            enc_value = data["Enc"][index]  # 현재 Enc 값

            if enc_value == 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item {id_value} 1")  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                
            else :
                # 띄어쓰기 포함한 입력
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@itemEnchant {id_value} 1 {enc_value}")  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터

            index += 1  # 인덱스 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

            

if __name__ == "__main__":
    print("세팅 시작")
    collection_item_setting()

