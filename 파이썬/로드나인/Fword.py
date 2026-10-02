import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def collection_item_setting():

    start_index = int(input("시작할 인덱스 번호를 입력하세요 (0부터 시작): "))

    a = """asshole
assjabber
assjacker
asslick
asslicker
assmonkey
assmucus
assmunch
assmuncher
asspirate
assshole
asssucker
asswad
asswhole
asswipe
autoerotic
b17ch
b1tch
backbojy
ballbag
ballsack
bangbros
bareback
bastard
beastial
beastiality
beefcurtain
beeotch
beeyotch
bestial
bestiality
biatch
bimbos
bitch
blowjob
blowme
bukkake
buttcheeks
butthole
buttpirate
buttplug
byatch
c0ck
c0cksucker
cameltoe
carpetmuncher
choad
choade
cl1t
clitface
clitlicker
clitoris
clits
clittylitter
cock
cokmuncher
corpwhore
cumbubble
cumchugger
cumdump
cumdumpster
cumfreak
cumguzzler
cumjockey
cummer
cumming
cumshot
cumslut
cumtart
cunilingus
cunillingus
cunnilingus
cunt
dick
ejaculate
ejaculating
ejaculatings
ejaculation
ejakulate
fuck
fatass
fcuk
fcuker
fcuking
feallatio
gaylord
gaysex
gaytard
gaywad
masterb8
masterbat3
masterbate
masterbation
masterbations
masturbate
n1gga
n1gger
nazi
nigaboo
nigg3r
nigg4h
nigga
niggah
niggas
niggaz
nigger
niggers
niglet
paedophile
pakki
palmpie
palmple
panooch
pecker
peckerhead
pedophile
pegging
pubic
punanny
pusse
pussi
pussies
pussy
puszy
queaf
queef
queerbait
queerhole
raping
rapist
rectum
retard
rimjob
rimming
sandnigger
scroat
scrote
scrotum
sh1t
shemale
shit
shiznit
sibal
skank
slut
sodding
sodoff
splooge
spooge
ssibal
ssibbal
ssipal
ssival
stfu
strapon
teabagging
teets
testical
testicle
towelhead
tranny
trannie
v14gra
v1gra
vagina
vajayjay
viagra
vjayjay
vulva
wetback
"""

    last_word = ""

    data = {
    "ID": a.split("\n")
    }


    index = start_index  # 초기 인덱스
    total_length = len(data["ID"])
    last_word = ""

    time.sleep(3)  # 실행 후 3초 대기 (입력 창 활성화를 위해)

    id_value = 0

    def should_stop():
        return keyboard.is_pressed("esc")

    def save_last_word(word):
        with open("last_word_log.txt", "w", encoding="utf-8") as f:
            f.write(word)

    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    pydirectinput.click(960, 570, button = 'left')
    time.sleep(0.1)
    

    while index < total_length:
        if should_stop():
            print("\n[ESC] 키로 중단되었습니다.")
            print(f"마지막으로 입력한 단어와 인덱스: {last_word}, {index}")
            break
        id_value = data["ID"][index]  # 현재 단어
        last_word = f"{id_value}" + " " + f"{index}"  # 마지막 단어 업데이트
        save_last_word(last_word)

        # 채팅창 클릭 후 명령어 입력
        pydirectinput.click(300, 1050)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()

        pyautogui.write(f"@test {id_value}")  # 명령어 입력
        time.sleep(0.1)

        # 엔터 클릭
        pydirectinput.click(700, 1050)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()


        index += 1
        time.sleep(0.5)  # 속도 조절

    else:
        print("모든 입력이 완료되었습니다!")
        print(f"마지막으로 입력한 단어와 인덱스: {last_word}," " " f"{index}")
        

if __name__ == "__main__":
    print("세팅 시작")
    collection_item_setting()

