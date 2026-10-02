import os
import hashlib

def get_file_hash(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        return hashlib.sha1(data).hexdigest()

def compare_files_in_folders(folder1, folder2):
    files1 = [f for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))]
    files2 = [f for f in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, f))]

    different_files = []
    for file1 in files1:
        if file1 in files2:
            file1_path = os.path.join(folder1, file1)
            file2_path = os.path.join(folder2, file1)
            if get_file_hash(file1_path) != get_file_hash(file2_path):
                different_files.append(file1)

    return different_files

folder1 = 'D:/OlderFile'
folder2 = 'D:/NewFile'

different_files = compare_files_in_folders(folder1, folder2)
if different_files:
    print("내용이 다른 파일 목록: ")
    for file in different_files:
        print("-", file)
else:
    print("내용이 다른 파일이 존재하지 않습니다.")
