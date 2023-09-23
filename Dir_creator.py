import os

file1 = open("Plan_badan.csv", "r")
file2 = open("Slownik.txt", "w")
next(file1)

plik = file1.readlines()
Dictionary = {}


def Path_creator(names):
    string = "{};{};{};{}".format(names[0], names[1], names[6], names[12])
    parent_dir = r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Foldery"
    path = os.path.join(parent_dir, string)
    return path

Number = 1
for names in plik:
    Names = names.replace("\n", "")
    Names = names.split(";")
    Name = 'Run_{}'.format(Number)
    Number += 1
    Path = Path_creator(Names)
#Temperatura, napięcie, woda anoda, woda katoda
    Lista = [Names[0],Names[1],Names[6],Names[12], Path]
    Dictionary[Name] = Lista

    # os.makedirs(path)
file2.write(str(Dictionary))
