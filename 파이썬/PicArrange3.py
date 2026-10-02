import os
import shutil
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import mean_squared_error
from skimage.exposure import equalize_hist

directory = 'D:\Yhakk\Result'

threshold = 0.4 # 유사도

for folder_name in sorted(os.listdir(directory)):
    if folder_name.startswith("group_") and int(folder_name.split("_")[1]) >= 61:
        folder_path = os.path.join(directory, folder_name)
        
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image = Image.open(os.path.join(folder_path, filename))
                image = equalize_hist(np.array(image.convert("L")))
                
                max_score = 0
                max_group = None
                for i in range(60):
                    group_folder_name = "group_" + str(i)
                    group_folder_path = os.path.join(directory, group_folder_name)
                    
                    for other_filename in os.listdir(group_folder_path):
                        if other_filename.endswith(".jpg") or other_filename.endswith(".png"):
                            other_image = Image.open(os.path.join(group_folder_path, other_filename))
                            
                            other_image = equalize_hist(np.array(other_image.convert("L")))
                            
                            score = compare_ssim(image, other_image, data_range=image.max() - image.min())
                            
                            if score >= threshold and score > max_score:
                                max_score = score
                                max_group = group_folder_name
                
                if max_group is not None:
                    new_folder_path = os.path.join(directory, max_group)
                    new_image_path = os.path.join(new_folder_path, filename)
                    shutil.move(os.path.join(folder_path, filename), new_image_path)
                    
dir_path = 'D:/Yhakk/Result'  
result_file = 'D:/Yhakk/Result/folder_counts.txt'

picture_counts = {}

for folder in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, folder)):
        if folder.startswith('group_'):
            group_number = folder[len('group_'):]
            picture_counts[group_number] = len(os.listdir(os.path.join(dir_path, folder)))

with open(result_file, 'w') as f:
    for group_number, count in sorted(picture_counts.items(), key=lambda x: int(x[0])):
        f.write(f"group_{group_number}: {count}\n")
