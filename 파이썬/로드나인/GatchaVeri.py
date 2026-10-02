import pyautogui
import keyboard
import time
import pydirectinput
import os
import math
import time
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import mean_squared_error
from skimage.exposure import equalize_hist

start = time.time()
count = 1
stop_flag = False
countValue = 100 # 몇회를 돌 것인지

directory = 'C:\STOVE\playwonder\Arena\Saved\Screenshots\WindowsClient' # 스크린샷 경로
directory2 = 'D:\Yhakk\Result' # 저장 경로

pydirectinput.click(1700, 974, button = 'left')     
time.sleep(0.5)  
pydirectinput.click(962, 704, button = 'left') 
time.sleep(0.5)
pyautogui.hotkey('esc')
time.sleep(0.5)

while count != countValue and not stop_flag: # 1로 바꾸면 무한 사이클
    pydirectinput.click(962, 993, button = 'left')
    time.sleep(3)
    pyautogui.hotkey('F9')
    time.sleep(0.5)
    pydirectinput.click(1749, 827, button = 'left')
    time.sleep(0.5)
    pyautogui.hotkey('esc')
    time.sleep(0.5)
    count += 1

    if keyboard.is_pressed('q'): # 즉시 중단 키
        stop_flag = True
    
pydirectinput.click(962, 993, button = 'left')
time.sleep(3)
pyautogui.hotkey('F9')
time.sleep(3)

for filename in os.listdir(directory): # 스크린샷 편집
    if filename.endswith('.jpg') or filename.endswith('.png'):
        
        image = Image.open(os.path.join(directory, filename))

        roi1 = image.crop((314, 510, 374, 570)) # 편집 위치 및 크기
        roi2 = image.crop((622, 510, 682, 570))
        roi3 = image.crop((930, 510, 990, 570))
        roi4 = image.crop((1238, 510, 1298, 570))
        roi5 = image.crop((1546, 510, 1606, 570))

        os.remove(os.path.join(directory, filename))

        roi1.save(os.path.join(directory2, 'roi1_' + filename))
        roi2.save(os.path.join(directory2, 'roi2_' + filename))
        roi3.save(os.path.join(directory2, 'roi3_' + filename))
        roi4.save(os.path.join(directory2, 'roi4_' + filename))
        roi5.save(os.path.join(directory2, 'roi5_' + filename))


threshold = 0.4 # 유사도
image_list = []

for filename in os.listdir(directory2):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(os.path.join(directory2, filename))
        # preprocess the image using histogram equalization
        image = equalize_hist(np.array(image.convert("L")))
        image_list.append((filename, image))

grouped_images = []
while image_list:
    filename, image = image_list.pop()
    similar_images = [(filename, image)]
    for i, (other_filename, other_image) in enumerate(image_list):
        score = compare_ssim(image, other_image, data_range=image.max() - image.min())
        if score >= threshold:
            similar_images.append((other_filename, other_image))
            image_list.pop(i)
    grouped_images.append(similar_images)

for i, images in enumerate(grouped_images):
    folder_name = "group_" + str(i)
    folder_path = os.path.join(directory2, folder_name)
    os.makedirs(folder_path)
    for j, (filename, image) in enumerate(images):
        image_path = os.path.join(directory2, filename)
        new_image_path = os.path.join(folder_path, filename)
        shutil.move(image_path, new_image_path)

dir_path = 'D:/Yhakk/Result'  
result_file = 'D:/Yhakk/Result/folder_counts.txt'

with open(result_file, 'w') as f:
    for folder in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, folder)):
            f.write(f"{folder}: {len(os.listdir(os.path.join(dir_path, folder)))}\n")

end = time.time()
print("총 실행 횟수 :",count)
print(f"소요시간 : {end - start:.5f} sec")

