import os

folder_path = r"D:\Yhakk\Result"

group_folders = [folder for folder in os.listdir(folder_path) if folder.startswith("group_")]

group_folders.sort(key=lambda x: len(os.listdir(os.path.join(folder_path, x))), reverse=True)

for index, folder in enumerate(group_folders):
    old_folder_path = os.path.join(folder_path, folder)
    temp_folder_name = f"temp_{index}"
    temp_folder_path = os.path.join(folder_path, temp_folder_name)
    os.rename(old_folder_path, temp_folder_path)

for index, folder in enumerate(group_folders):
    temp_folder_name = f"temp_{index}"
    new_folder_name = f"group_{index}"
    temp_folder_path = os.path.join(folder_path, temp_folder_name)
    new_folder_path = os.path.join(folder_path, new_folder_name)
    os.rename(temp_folder_path, new_folder_path)

print("재정렬 완료 : ")
for folder in group_folders:
    print(folder)
