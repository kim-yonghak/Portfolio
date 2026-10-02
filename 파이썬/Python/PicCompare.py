import pyautogui
import keyboard
import time
import pydirectinput
import os
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim

directory2 = 'D:\Yhakk\Result'

# Set the similarity threshold (0 to 1)
threshold = 0.5

# Load images from the folder
image_list = []
for filename in os.listdir(directory2):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(os.path.join(directory2, filename))
        image_list.append(np.array(image.convert("L")))

# Compare images using SSIM and group similar ones
grouped_images = []
while image_list:
    image = image_list.pop()
    similar_images = [image]
    for i, other_image in enumerate(image_list):
        score = compare_ssim(image, other_image)
        if score >= threshold:
            similar_images.append(other_image)
            image_list.pop(i)
    grouped_images.append(similar_images)

# Save the grouped images to a new folder
for i, images in enumerate(grouped_images):
    folder_name = "group_" + str(i)
    folder_path = os.path.join(directory2, folder_name)
    os.makedirs(folder_path)
    for j, image in enumerate(images):
        image_name = "image_" + str(j) + ".jpg"
        image_path = os.path.join(folder_path, image_name)
        Image.fromarray(image).save(image_path)
