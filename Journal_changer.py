import ast
file1 = open(r"C:\Users\mprze\Desktop\Folder_pulpit\Rysunki\Nowy_journal", "r")
file2 = open("Journal_edytowany.jou", "w")
file3 = open("Slownik.txt", "r")
file4 = open("Plan_badan.csv", "r")

list = file1.readlines()



dictionary = file3.readlines()
dictionary = ast.literal_eval(dictionary[0])

next(file4)
list_of_parameters = file4.readlines()
print(len(list_of_parameters))
print(len(dictionary))
#######################################################################################################################################

def Voltage(Line, V):
    if "Total Voltage (V)" in Line: 
        Line = Line.replace('0.4', V)
        return Line
    else:
        return Line

def Temperature(Line, T):
    if "[K]" in  Line:
        Line = Line.replace('333', T)
        return Line
    else:
        return Line

########################################################################################################################################

def Mass_flow_anode(Line, Mfa):
    if "Expression*Table1*ExpressionEntry3(Definition)\" '(\"1.41e-7 [kg/s]" in Line:
        Line = Line.replace('1.41e-7', Mfa)
        return Line
    else:
        return Line

def Mass_flow_cathode(Line, Mfc):
    if "Expression*Table1*ExpressionEntry3(Definition)\" '(\"1.1e-6 [kg/s]" in Line:
        Line = Line.replace('1.1e-6', Mfc)
        return Line
    else:
        return Line

######################################################################################################################################

def Anode_inlet_hydrogen_stoichiometry(Line, H2):
    if "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table1*ExpressionEntry1(h2)\" '(\"0.6" in Line:
        Line = Line.replace('0.6', H2)
        return Line
    else:
        return Line

def Anode_inlet_water_stoichiometry(Line, H2O):
    if "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.2" in Line:
        Line = Line.replace('0.2', H2O)
        return Line
    else:
        return Line

def Cathode_inlet_oxygen_stoichiometry(Line, O2):
    if "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table2*ExpressionEntry1(o2)\" '(\"0.21" in Line:
        Line = Line.replace('0.21', O2)
        return Line
    else:
        return Line

def Cathode_inlet_water_stoichiometry(Line, H2O):
    if "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.11" in Line:
        Line = Line.replace('0.11', H2O)
        return Line
    else:
        return Line
    
################################################################################################################################

def Anode_outlet_hydrogen_stoichiometry(Line, H2):
    if "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table1*ExpressionEntry1(h2)\" '(\"0.211" in Line:
        Line = Line.replace('0.211', H2)
        return Line
    else:
        return Line

def Anode_outlet_water_stoichiometry(Line, H2O):
    if "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.111" in Line:
        Line = Line.replace('0.111', H2O)
        return Line
    else:
        return Line
    
def Cathode_outlet_oxygen_stoichiometry(Line, O2):
    if "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table2*ExpressionEntry1(o2)\" '(\"0.212" in Line:
        Line = Line.replace('0.212', O2)
        return Line
    else:
        return Line
    
def Cathode_outlet_water_stoichiometry(Line, H2O):
    if "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.112" in Line:
        Line = Line.replace('0.112', H2O)
        return Line
    else:
        return Line


##########################################################################################################################

def Line_changer(Line, **kwargs):
    if "Total Voltage (V)" in  Line and 'V' in kwargs:
        return(Voltage(Line, kwargs['V']))
    elif "[K]" in  Line and 'T' in kwargs:
        return(Temperature(Line, kwargs['T']))
    elif "Expression*Table1*ExpressionEntry3(Definition)\" '(\"1.41e-7 [kg/s]" in Line and 'Mfa' in kwargs:
        return(Mass_flow_anode(Line, kwargs['Mfa']))
    elif "Expression*Table1*ExpressionEntry3(Definition)\" '(\"1.1e-6 [kg/s]" in Line and 'Mfc' in kwargs:
        return(Mass_flow_cathode(Line, kwargs['Mfc']))
    elif "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table1*ExpressionEntry1(h2)\" '(\"0.6" in Line and 'AIH2' in kwargs:
        return(Anode_inlet_hydrogen_stoichiometry(Line, kwargs['AIH2']))
    elif "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.2" in Line and 'AIH2O' in kwargs:
        return(Anode_inlet_water_stoichiometry(Line, kwargs['AIH2O']))
    elif "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table2*ExpressionEntry1(o2)\" '(\"0.21" in Line and 'CIO2' in kwargs:
        return(Cathode_inlet_oxygen_stoichiometry(Line, kwargs['CIO2']))
    elif "Mass-Flow Inlet*Frame2*Frame2*Frame4(Species)*Table1*Table2(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.11" in Line and 'CIH2O' in kwargs:
        return(Cathode_inlet_water_stoichiometry(Line, kwargs['CIH2O']))
    elif "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table1*ExpressionEntry1(h2)\" '(\"0.211" in Line and 'AOH2' in kwargs:
        return(Anode_outlet_hydrogen_stoichiometry(Line, kwargs['AOH2']))
    elif "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.111" in Line and 'AOH2O' in kwargs:
        return(Anode_outlet_water_stoichiometry(Line, kwargs['AOH2O']))
    elif "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table2*ExpressionEntry1(o2)\" '(\"0.212" in Line and 'COO2' in kwargs:
        return(Cathode_outlet_oxygen_stoichiometry(Line, kwargs['COO2']))
    elif "Pressure Outlet*Frame2*Frame2*Frame4(Species)*Table1*Table6(Species Mass Fractions)*Table3*ExpressionEntry1(h2o)\" '(\"0.112" in Line and 'COH2O' in kwargs:
        return(Cathode_outlet_water_stoichiometry(Line, kwargs['COH2O']))
    else:
        return(Line)


# file2.write(list[0])
z = 0
for keys in dictionary:
    print(keys)
    list_parameters = list_of_parameters[z]
    list_parameters = list_parameters.split(";")
    T = list_parameters[0]
    V = list_parameters[1]
    AIH2O = list_parameters[6]
    CIH2O = list_parameters[12]
    z += 1    
    for i in range(1, (len(list) - 2)):
        Line_checker = list[i]
        file2.write(Line_changer(Line_checker, V = V, T = T, AIH2O = AIH2O, CIH2O = CIH2O))
    file2.write("\n")

file2.write(list[-2])