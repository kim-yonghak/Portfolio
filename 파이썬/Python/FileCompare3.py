import os
import hashlib
import difflib

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

def print_differences(folder1, folder2, file):
    file1_path = os.path.join(folder1, file)
    file2_path = os.path.join(folder2, file)

    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    differences = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1_path, tofile=file2_path)

    print('\n내용이 다른 부분 {}:'.format(file))
    for line in differences:
        print(line)

folder1 = 'D:/OlderFile'
folder2 = 'D:/NewFile'

different_files = compare_files_in_folders(folder1, folder2)
if different_files:
    print("내용이 다른 파일 목록: ")
    for file in different_files:
        print("-", file)
else:
    print("내용이 다른 파일이 존재하지 않습니다.")

for file in different_files:
    print_differences(folder1, folder2, file)
