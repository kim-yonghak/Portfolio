import os
import shutil
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import mean_squared_error
from skimage.exposure import equalize_hist

directory = 'D:\Yhakk\Result'
directory2 = 'D:\Yhakk\Result'

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
