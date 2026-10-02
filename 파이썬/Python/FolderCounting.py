import os

dir_path = 'D:/Yhakk/Result'  # Replace with your directory path
result_file = 'D:/Yhakk/folder_counts.txt'    # Replace with desired output file name

with open(result_file, 'w') as f:
    for folder in os.listdir(dir_path):
        if os.path.isdir(os.path.join(dir_path, folder)):
            f.write(f"{folder}: {len(os.listdir(os.path.join(dir_path, folder)))}\n")
