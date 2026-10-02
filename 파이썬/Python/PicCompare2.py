import os
import shutil
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim
from skimage.metrics import mean_squared_error
from skimage.exposure import equalize_hist

directory = 'D:\Yhakk\Result'

# Set the threshold for similarity
threshold = 0.4

# Loop over the folders with names starting from "group_61"
for folder_name in sorted(os.listdir(directory)):
    if folder_name.startswith("group_") and int(folder_name.split("_")[1]) >= 61:
        folder_path = os.path.join(directory, folder_name)
        
        # Loop over the images in this folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image = Image.open(os.path.join(folder_path, filename))
                
                # Preprocess the image using histogram equalization
                image = equalize_hist(np.array(image.convert("L")))
                
                # Loop over the previous groups and compare with the current image
                max_score = 0
                max_group = None
                for i in range(60):
                    group_folder_name = "group_" + str(i)
                    group_folder_path = os.path.join(directory, group_folder_name)
                    
                    # Loop over the images in this group folder and compare with the current image
                    for other_filename in os.listdir(group_folder_path):
                        if other_filename.endswith(".jpg") or other_filename.endswith(".png"):
                            other_image = Image.open(os.path.join(group_folder_path, other_filename))
                            
                            # Preprocess the other image using histogram equalization
                            other_image = equalize_hist(np.array(other_image.convert("L")))
                            
                            # Calculate the similarity score
                            score = compare_ssim(image, other_image, data_range=image.max() - image.min())
                            
                            # If the score is higher than the threshold and the highest score so far,
                            # update the max score and the folder that contains the most similar images
                            if score >= threshold and score > max_score:
                                max_score = score
                                max_group = group_folder_name
                
                # If there is a folder that contains the most similar images,
                # move the current image to that folder
                if max_group is not None:
                    new_folder_path = os.path.join(directory, max_group)
                    new_image_path = os.path.join(new_folder_path, filename)
                    shutil.move(os.path.join(folder_path, filename), new_image_path)
