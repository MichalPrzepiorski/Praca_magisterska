import linecache

file1 = open('Plik_wyniki.prof')
file2 = open('Plik_wyniki.csv', 'w')

def Line_counter():
    c = 0
    for line in file1:
        if line.startswith('('):
            continue
        elif line.startswith(')'):
            break
        else:
            c += 1
    file1.seek(0)
    file2.seek(0)
    return c

c = Line_counter()

def Data_conversion(line1, line2, line3, line4):
    linemod1 = line1.strip()
    linemod2 = line2.strip()
    linemod3 = line3.strip()
    linemod4 = line4.strip()
    linenew = '%s;%s;%s;%s;\n' % (linemod1, linemod2, linemod3, linemod4)
    return linenew

def Line_checker(line):
    if line.startswith('(x') or line.startswith('(y') or line.startswith('(z') or line.startswith('(current'):
        return True
    else:
        return False
    
def Line_skipper(line):
    if line.startswith('(') or line.startswith(')'):
        return True
    else:
        return False

def File_scanner():
    List_of_elements = []
    for i, lines in enumerate(file1):
        if Line_checker(lines):
            List_of_elements.append(i+1)
        else:
            continue
    file1.seek(0)
    return List_of_elements


def Creating_header():
    Header = ''
    File_scanner_list = File_scanner()
    for Number in File_scanner_list:
        String1 = linecache.getline(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Praca_magisterska\Plik_wyniki.prof", int(Number))
        String2 = String1.strip()
        String3 = String2.replace(String2[0], "", 1)
        String4  = '%s;' % (String3)
        Header += String4
    Header = '%s\n' % (Header)
    file1.seek(0)
    return Header

file2.write(Creating_header())

file1.seek(0)


for i, Line in enumerate(file1):
    if i < c+2:
        if Line_skipper(Line):
            continue
        else:
            String = Data_conversion(str(Line),\
            str(linecache.getline(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Praca_magisterska\Plik_wyniki.prof", i+c+3)),\
            str(linecache.getline(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Praca_magisterska\Plik_wyniki.prof", i+2*c+5)),\
            str(linecache.getline(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Praca_magisterska\Plik_wyniki.prof", i+3*c+7)))
            file2.write(String)
            file1.seek
    else:
        break

file1.close
file2.close


#https://pynative.com/python-read-specific-lines-from-a-file/


    

  



