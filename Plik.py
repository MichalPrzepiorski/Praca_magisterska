import pandas as pd


file1 = open('Plik_wyniki.prof')

Plik = file1.readlines()
file1.seek(0)


def Line_counter_prime():
    Plik = file1.readlines()
    file1.seek(0)
    List = Plik[0]
    List = List.split()
    String = List[2]
    String = String.replace(")", "")
    String = int(String)
    return String


def Rows_indexes(Number_of_rows):
    List_of_rows = []
    for i in range(4):
        Start = 3
        Start = Start + Number_of_rows*i + 2*i -1
        End = Start + Number_of_rows 
        List_of_rows.append([Start, End])
    return(List_of_rows)

List_of_rows = Rows_indexes(Line_counter_prime())

data = {}

df = pd.DataFrame(data)

df = df.replace('\n','', regex=True)

List = Rows_indexes(Line_counter_prime())
print(List)
List_of_rows1 = List_of_rows[0]
df['x'] = Plik[List_of_rows1[0]:List_of_rows1[1]]
List_of_rows2 = List_of_rows[1]
print(List_of_rows)
df['y'] = Plik[List_of_rows2[0]:List_of_rows2[1]]   
List_of_rows3 = List_of_rows[3]
df['total_temperature'] = Plik[List_of_rows3[0]:List_of_rows3[1]]
df = df.replace('\n','', regex=True)
print(df)
df.to_csv('Wynik.csv', index=False, sep=";")
    
file1.close()
  



