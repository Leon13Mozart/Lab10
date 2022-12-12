import os
import shutil

folder_path = "C:\\Program Files\\" # - шлях до папки з якої будуть копіюваться файли
folder_list = os.listdir(folder_path)

print(folder_list)

parent_dir = "C:" # - шлях до папки в якій створиться папка RESULTS
new_dir = "RESULTS"
path_dir = os.path.join(parent_dir, new_dir)
os.mkdir (path_dir)

for i in range(2):
    src_file = os.path.join(folder_path, folder_list[i])
    dst_file = os.path.join(path_dir, folder_list[i])
    shutil.copyfile(src_file, dst_file)