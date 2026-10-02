import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def enchant_weapon_setting():
    strt = input("티어를 선택해주세요(영웅 = 1, 전설 = 2, 신화 = 3): ")
    strw = input("망토 타입을 선택해주세요(전투 = 1, 파괴 = 2, 정령 = 3, 용맹 = 4): ")
    w = int(strw)
    t = int(strt)
    weapon_code = 0

    if w == 1:
        weapon_code += 121600101
        if t == 1:
            weapon_code += 50000
        elif t == 2:
            weapon_code += 60000
        elif t == 3:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 2:
        weapon_code += 122600101
        if t == 1:
            weapon_code += 50000
        elif t == 2:
            weapon_code += 60000
        elif t == 3:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 3:
        weapon_code += 123600101
        if t == 1:
            weapon_code += 50000
        elif t == 2:
            weapon_code += 60000
        elif t == 3:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()
    elif w == 4:
        weapon_code += 124600101
        if t == 1:
            weapon_code += 50000
        elif t == 2:
            weapon_code += 60000
        elif t == 3:
            weapon_code += 70000
        else :
            print("잘못된 티어를 입력하셨습니다!")
            enchant_weapon_setting()

    else :
        print("잘못된 망토를 입력하셨습니다!")
        enchant_weapon_setting()
           
    if t == 1:
        enchant_point = 4
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(8):
            str2 = str(weapon_code)
            for i in range(4):
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
                if enchant_point == 4:
                    enchant_point = 5
                elif enchant_point == 5:
                    enchant_point = 8
                elif enchant_point == 8:
                    enchant_point = 20
            weapon_code += 1
            enchant_point = 4

        print("종료되었습니다. \n")
        enchant_weapon_setting()

    if t == 2:
        enchant_point = 3
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(6):
            str2 = str(weapon_code)
            for i in range(4):
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
                if enchant_point == 3:
                    enchant_point = 4
                elif enchant_point == 4:
                    enchant_point = 7
                elif enchant_point == 7:
                    enchant_point = 20
            weapon_code += 1
            enchant_point = 3

        print("종료되었습니다. \n")
        enchant_weapon_setting()
            
    if t == 3:
        enchant_point = 2
        str1 = "@itemEnchant "
        str3 = " 1 "
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        pydirectinput.click(960, 570, button = 'left')
        time.sleep(0.1)
        
        for i in range(1):
            str2 = str(weapon_code)
            for i in range(4):
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
                if enchant_point == 2:
                    enchant_point = 3
                elif enchant_point == 3:
                    enchant_point = 6
                elif enchant_point == 6:
                    enchant_point = 20
            weapon_code += 1
            enchant_point = 2

        print("종료되었습니다. \n")
        enchant_weapon_setting()


if __name__ == "__main__":
    print("세팅 시작")
    enchant_weapon_setting()

