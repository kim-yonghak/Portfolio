import pyautogui
import keyboard
import time
import pydirectinput
import keyboard
    
def collection_item_setting():

    start_index = int(input("시작할 인덱스 번호를 입력하세요 (0부터 시작): "))

    a = """admin
administrator
asshole
asshopper
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
autonick
b17ch
b1tch
ballbag
ballsack
bangbros
bareback
bastard
beaner
beastiality
beefcurtain
beeotch
beeyotch
bestiality
biatch
bimbos
bitch
blowjob
blowme
boner
bukkake
butthole
buttplug
byatch
c0ck
c0cksucker
cameltoe
cawk
chinc
circlejerk
clevelandsteamer
clit
clitlicker
clitoris
cock
cokmuncher
coksucka
coochie
coochy
cumchugger
cumdumpster
cumfreak
cumguzzler
cumbubble
cumdump
cumjockey
cummer
cumming
cums
cumshot
cumslut
cumtart
cunilingus
cunillingus
cunnilingus
cunt
cyberfuc
d1ck
dago
dick
dike
dildo
doggiestyle
doochbag
doosh
douchebag
douchefag
douchenozzle
douchewaffle
duche
dumass
dumbass
dyke
ejaculate
ejaculating
ejaculatings
ejaculation
ejakulate
epic7
erotic
fuck
facebook
facial
fack
fag
fatass
fcuk
fcuker
fcuking
feallatio
fecal
fellate
fellatio
fetish
fook
fooker
footjob
fudgepacker
fuk
fux
fux0r
gangbang
gangbanged
gangbangs
gassyass
gayass
gaybob
gaydo
gaylord
gaysex
gaytard
gaywad
gm
goatse
goldenshower
gooch
google
gook
gringo
gtfo
guido
handjob
hardcoresex
hardon
heshe
hitler
hoar
hoare
hoer
homo
homoerotic
honkey
hore
horniest
hotsex
humping
jackass
jackoff
jagoff
jerkass
jerkoff
jizm
jizz
juggs
junglebunny
kawk
kike
kinkyjesus
knobend
knobhead
knobjocky
knobjokey
kock
kondum
kondums
kooch
kootch
kraut
kummer
kumming
kunilingus
kunt
kyke
l3itch
labia
lameass
lardass
lesbo
lezbo
lezzie
logflogger
lusting
m0f0
m0fo
m45terbate
ma5terb8
ma5terbate
mafugly
masochist
masterb8
masterbat3
masterbate
masterbation
masterbations
masturbate
megaport
mfer
milf
minge
mof0
mofo
muff
muffdiver
muffpuff
munging
muthafecker
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
nipples
nobhead
nobjocky
nobjokey
numbnuts
nutbutter
nutsack
orgasim
orgasims
orgasm
orgasms
orgy
p0rn
p1ss
paedophile
paimpie
paimple
pakki
palmpie
palmple
panooch
pecker
peckerhead
pedophile
pegging
penis
penisbanger
penisfucker
penispuffer
phonesex
phuck
phuk
phuked
phuking
phukked
phukking
phuks
phuq
pigfucker
pimpis
pissed
pissedoff
pisser
pissers
pisses
pissflaps
pissin
pissing
pissoff
polesmoker
pollack
poofter
poonani
poonany
poontang
poopchute
porchmonkey
porn
porno
pornography
pornos
prick
pron
pube
pubic
punanny
pusse
pussi
pussies
pussy
pussyfart
pussylicking
pussys
puszy
queaf
queef
queer
queerbait
queerhole
rape
raping
rapist
rectum
retard
rimjaw
rimjob
rimming
ruski
sadism
sadist
sandbar
sandnigger
schlong
scroat
scrote
scrotum
sggm
sgmegaport
sh1t
shagger
shaggin
shagging
shemale
shit
shiz
shiznit
sibal
skank
slut
sm11egate
sm11egategm
sm11egategms
sm1legate
sm1legategm
sm1legategms
smeg
smegma
smi1egate
smi1egategm
smi1egategms
smiiegate
smiiegategm
smiigategms
smilegate
smilegategm
smilegategms
smut
sodding
sodoff
spick
splooge
spooge
ssibal
ssibbal
ssipal
ssival
stfu
stove
strapon
suckass
sucker
sucksex
supercreative
t1tt1e5
t1tties
tard
tardo
teabagging
teets
testical
testicle
threesome
titwank
tittie5
tittiefucker
titties
tittyfuck
tittys
tittywank
towelhead
tranny
trannie
turd
turdburglar
tw4t
twat
twunt
twunter
unclefucker
v14gra
v1gra
vagina
vajayjay
viagra
vjayjay
vulva
w00se
wang
wank
wanker
wankjob
wanky
wetback
whoar
whore
xrated
zazi
zot
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
        pydirectinput.click(1035, 325)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()

        pyautogui.write(f"{id_value}")  # 명령어 입력
        time.sleep(0.1)

        # 엔터 클릭
        pydirectinput.click(970, 865)
        pydirectinput.mouseDown()
        pydirectinput.mouseUp()


        index += 1
        time.sleep(1)  # 속도 조절

    else:
        print("모든 입력이 완료되었습니다!")
        print(f"마지막으로 입력한 단어와 인덱스: {last_word},")
        

if __name__ == "__main__":
    print("세팅 시작")
    collection_item_setting()

