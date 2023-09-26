import os
import shutil
import time

file1 = open("Plan_badan.csv", "r")
file2 = open("Slownik.txt", "w")
next(file1)

plik = file1.readlines()
print(len(plik))
Dictionary = {}


def Path_creator(names):
    string = "{};{};{};{}".format(names[0], names[1], names[6], names[12])
    parent_dir = r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Foldery"
    path = os.path.join(parent_dir, string)
    return path

original1 = r'C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Prof_to_csv_all.py'
original3 = r'C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Current_density.prof'
original4 = r'C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Temperature.prof'
Number = 1
for names in plik:
    Names = names.replace("\n", "")
    Names = names.split(";")
    Name = 'Run_{}'.format(Number)
    print(Name)
    Number = Number + 1
    Path = Path_creator(Names)
#Temperatura, napięcie, woda anoda, woda katoda
    Lista = [Names[0], Names[1], Names[6], Names[12], Path]
    Dictionary[Name] = Lista
file2.write(str(Dictionary))
    # os.makedirs(Path)
    # shutil.copy(original1, Path)
    # shutil.copy(original3, Path) 
    # shutil.copy(original4, Path)
    # time.sleep(0.5)
    # os.system("python {}\\Prof_to_csv_all.py".format(Path))
    # time.sleep(2)

