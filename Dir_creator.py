import os

for i in range(10):
    directory = "Folder_{}".format(i)
    parent_dir = r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki"
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)