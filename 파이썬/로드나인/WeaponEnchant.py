import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def enchant_weapon_setting():
    strt = input("티어를 선택해주세(희귀 = 1, 영웅 = 2, 전설 = 3, 신화 = 4): ")
    strw = input("무기를 선택해주세요(권갑 = 1, 검/방패 = 2, 전투봉 = 3, 전투 방패 = 4, 대검 = 5, 지팡이 = 6, 단검 = 7, 활 = 8, 석궁 = 9): ")
    w = int(strw)
    t = int(strt)
    weapon_code = 0

    if w == 1:
        weapon_code += 110100101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 2:
        weapon_code += 111000101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 3:
        weapon_code += 111200101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 4:
        weapon_code += 112000101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 5:
        weapon_code += 112100101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 6:
        weapon_code += 112300101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 7:
        weapon_code += 113100101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 8:
        weapon_code += 114000101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 9:
        weapon_code += 114200101
        if t == 1:
            weapon_code += 40000
        elif t == 2:
            weapon_code += 50000
        elif t == 3:
            weapon_code += 60000
        elif t == 4:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    else :
        print("잘못된 무기를 입력하셨습니다!")
        enchant_weapon_setting()
           
    if t == 1:
        enchant_point = 11
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(10):
            str2 = str(weapon_code)
            for i in range(10):
                str4 = str(enchant_point)
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                time.sleep(0.1)
                pyautogui.write(str1 + str2 + str3 + str4)
                time.sleep(0.1)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                enchant_point += 1
            weapon_code += 1
            enchant_point = 11

        print("종료되었습니다. \n")
        enchant_weapon_setting()

    if t == 2:
        enchant_point = 9
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(8):
            str2 = str(weapon_code)
            for i in range(12):
                str4 = str(enchant_point)
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                time.sleep(0.1)
                pyautogui.write(str1 + str2 + str3 + str4)
                time.sleep(0.1)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                enchant_point += 1
            weapon_code += 1
            enchant_point = 9

        print("종료되었습니다. \n")
        enchant_weapon_setting()
            
    if t == 3:
        enchant_point = 8
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(6):
            str2 = str(weapon_code)
            for i in range(13):
                str4 = str(enchant_point)
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                time.sleep(0.1)
                pyautogui.write(str1 + str2 + str3 + str4)
                time.sleep(0.1)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                enchant_point += 1
            weapon_code += 1
            enchant_point = 8
            
        print("종료되었습니다. \n")
        enchant_weapon_setting()

    if t == 4:
        enchant_point = 7
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(1):
            str2 = str(weapon_code)
            for i in range(14):
                str4 = str(enchant_point)
                pydirectinput.click(300, 1050, button = 'left')
                pydirectinput.mouseDown() 
                pydirectinput.mouseUp()
                time.sleep(0.1)
                pyautogui.write(str1 + str2 + str3 + str4)
                time.sleep(0.1)
                pydirectinput.click(700, 1050, button = 'left')
                pydirectinput.mouseDown() #엔터
                pydirectinput.mouseUp() #엔터
                enchant_point += 1
            weapon_code += 1
            enchant_point = 7

        print("종료되었습니다. \n")
        enchant_weapon_setting()


if __name__ == "__main__":
    print("세팅 시작")
    enchant_weapon_setting()

