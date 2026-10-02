import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def collection_item_setting():
    strt = input("순서를 선택해주세요(1, 2, 3): ")
    t = int(strt)

    a = """19997382
19997383
19997384
19997385
19997390
19997391
19997392
19997393
19997350
19997351
19997352
19997353
19997354
19997355
19997356
19997357
19997358
19997359
19997360
19997361
19997362
19997363
19997364
19997365
19997366
19997367
19997368
19997369
19997345
19997346
19997347
19997348
19997370
19997371
19997372
19997373
19997334
19997335
19997336
19997337
19997291
19997292
19997293
19997294
19997295
19997296
19997297
19997298
19997299
19997300
19997301
19997302
19997303
19997304
19997305
19997306
19997307
19997308
19997309
19997320
19997400
"""
    
    b = """75
75
75
75
75
75
75
75
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
45
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
15
10
"""
    
    ID1 = ",".join(a.split("\n"))
    Enc1 = ",".join(b.split("\n"))

    data = { "ID": ID1.split(","),
             "Enc" : list(map(int, filter(None, Enc1.split(","))))
             }


    index = 0  # 초기 인덱스
    cnt = 0 # 초기 개수
    total_length = len(data["ID"])
    total_cnt = sum(data["Enc"])
    half_index = total_length // 2
    half_cnt = total_cnt // 2

    first_index = 450
    second_index = 900

    first_cnt = 450
    second_cnt = 900

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


            if enc_value != 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item {id_value} {enc_value}", interval=0)  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터


            index += 1 # 인덱스 증가
            cnt += enc_value  # 카운트 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

    if t == 2:
        index = first_index
        while index < second_index:
            id_value = data["ID"][index]  # 현재 ID 값
            enc_value = data["Enc"][index]  # 현재 Enc 값

            if enc_value != 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item {id_value} {enc_value}", interval=0)  # 띄어쓰기 추가
                time.sleep(0.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터

            index += 1 # 인덱스 증가
            cnt += enc_value  # 카운트 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

    if t == 3:
        index = second_index
        while index < total_index:
            id_value = data["ID"][index]  # 현재 ID 값
            enc_value = data["Enc"][index]  # 현재 Enc 값

            if enc_value != 0:
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                pyautogui.write(f"@item 1{id_value} {enc_value}", interval=0)  # 띄어쓰기 추가
                time.sleep(1.5)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터

            index += 1 # 인덱스 증가
            cnt += enc_value  # 카운트 증가
            time.sleep(0.5)  # 입력 속도 조절

        print("모든 입력이 완료되었습니다!")

            

if __name__ == "__main__":
    print("세팅 시작")
    collection_item_setting()

