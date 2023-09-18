file1 = open(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Journal_testowy", "r")
file2 = open("Journal_edytowany.jou", "w")
list = file1.readlines()

def Voltage(Line, V):
    Line = Line.replace('0.4', V)
    return Line

def Temperature(Line, T):
    if "Expression*Table1*ExpressionEntry3(Definition)" in  Line:
        Line = Line.replace('323', T)
        return Line
    else:
        return Line

def Mass_flow_anode():
    """dsgasgd"""

def Mass_flow_cathode():
    """sggasdgaas"""

def Anode_hydrogen_stoichiometry():
    """asfsa"""

def Anode_water_stoichiometry():
    """asfsa"""

def Cathode_oxygen_stoichiometry():
    """asfsa"""

def Cathode_water_stoichiometry():
    """asfsa"""

def Line_changer(Line, **kwargs):
    if "Total Voltage (V)" in  Line and 'V' in kwargs:
        return(Voltage(Line, kwargs['V']))
    else:
        return(Temperature(Line, kwargs['T']))




z = 0
file2.write(list[0])
while z <= 2:
    z += 1
    print("chuj")
    for i in range(1, (len(list) - 2)):
        Line_checker = list[i]
        file2.write(Line_changer(Line_checker, V = "0.7", T = "323"))
    if z <= 2:
        file2.write("\n")
    else:
        pass
file2.write(list[-2])