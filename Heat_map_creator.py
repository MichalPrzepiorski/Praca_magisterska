import pandas as pd
import matplotlib.pyplot as plt

def Function(Csv_file):
    file_to_open = Csv_file

    def Changer(Argument):
        global file_to_open 
        file_to_open = Argument


    file1 = open(file_to_open, 'r')
    List_names = file1.readlines()
    file1.close()

    df = pd.read_csv(file_to_open, sep=';')
    pd.options.display.max_rows = 10 

    List_names = List_names[0]
    List_names = List_names.split(";")
    List_names = List_names[3]
    List_names = List_names.replace("\n", "")
    Z_name = List_names


    X = df['x'].round(5)
    Y = df['y'].round(5)
    Z = df[Z_name].round(5)


    X_min = X.min()
    X_max = X.max()
    Y_min = Y.min()
    Y_max = Y.max()

    X_cells_horizontal = 10
    Y_cells_vertical = 7

    def X_lines(Number_of_cells_in_x_axis):
        List_of_x_lines = [X_min]
        Width = ((X_max - X_min)/Number_of_cells_in_x_axis)
        for i in range(Number_of_cells_in_x_axis-1):
            X_append = X_min+(i+1)*Width
            List_of_x_lines.append(round(X_append, 5))
        List_of_x_lines.append(X_max)
        return List_of_x_lines

    def Y_lines(Number_of_cells_in_x_axis):
        List_of_y_lines = [Y_min]
        Width = ((Y_max - Y_min)/Number_of_cells_in_x_axis)
        for i in range(Number_of_cells_in_x_axis-1):
            Y_append = Y_min+(i+1)*Width
            List_of_y_lines.append(round(Y_append, 5))
        List_of_y_lines.append(Y_max)
        return List_of_y_lines

    def Centers_of_cells_by_X(List_of_x_lines):
        List_of_x_cells_centers_cord = []
        for i in range(len(List_of_x_lines)):
            if i == 0:
                continue
            else:
                X_cord = ((List_of_x_lines[i] - List_of_x_lines[i - 1])/2)+List_of_x_lines[i - 1]
                List_of_x_cells_centers_cord.append(round(X_cord,5))
        return List_of_x_cells_centers_cord

    def Centers_of_cells_by_Y(List_of_y_lines):
        List_of_y_cells_centers_cord = []
        for i in range(len(List_of_y_lines)):
            if i == 0:
                continue
            else:
                Y_cord = ((List_of_y_lines[i] - List_of_y_lines[i - 1])/2)+List_of_y_lines[i - 1]
                List_of_y_cells_centers_cord.append(round(Y_cord,5))
        return List_of_y_cells_centers_cord

    def List_creator(List, position):
        Empty_list = []
        for i in range(len(List)):
            Empty_list.append(List[position])
        return Empty_list


    def Dict_creator():
        X_boundaries = X_lines(X_cells_horizontal)
        Y_boundaries = Y_lines(Y_cells_vertical)
        Dict_of_df = {}
        for i in range(1, len(X_boundaries)):
            for z in range(1, len(Y_boundaries)):
                Dict_of_df['Komorka_%s%s' % (i, z)] = df.loc[(df['x'] <= X_boundaries[i] + 0.00012) & (df['x'] >= X_boundaries[i - 1] - 0.00012)\
                & (df['y'] <= Y_boundaries[z]) & (df['y'] >= Y_boundaries[z - 1])]
        return Dict_of_df

    filehandler = open('filename.txt', 'wt')
    data = str(Dict_creator())
    filehandler.write(data)

    def Cells_centers_dict():
        X_centers = Centers_of_cells_by_X(X_lines(X_cells_horizontal))
        Y_centers  = Centers_of_cells_by_Y(Y_lines(Y_cells_vertical))
        Dict_of_cells = {}
        x = 1
        y = 1
        for X_cen in X_centers:
            for Y_cen in Y_centers:
                Dict_of_cells['Komorka_%s%s' % (x, y)] = [X_cen, Y_cen]
                y += 1
            x += 1
            y = 1
        return Dict_of_cells

    filehandler = open('filename2.txt', 'wt')
    data = str(Cells_centers_dict())
    filehandler.write(data)

    def Wieght_average_of_points():
        New_dict1 = Dict_creator()
        New_dict2 = Cells_centers_dict()
        for key in New_dict1:
            operator = New_dict1[key]
            operator.drop(columns = ['z'], inplace=True) 
            position = New_dict2[key]
            operator['x'] = operator['x'].apply(lambda x: x - position[0])
            operator['y'] = operator['y'].apply(lambda y: y - position[1])
            operator['weight'] = 1.0/(((operator ['x']**2)+(operator['y']**2))**(1.0/2.0))
        return(New_dict1)

    filehandler = open('filename3.txt', 'wt')
    data = str(Wieght_average_of_points())
    filehandler.write(data)


    def Average_weight():
        dictionary = Wieght_average_of_points()
        Weight_dictionary = {}
        for keys in dictionary:
            operator = dictionary[keys]
            weighted_average = sum(operator[Z_name]*operator['weight'])/operator['weight'].sum()
            Weight_dictionary[keys] = weighted_average
        return(Weight_dictionary)


    filehandler = open('filename4.txt', 'wt')
    data = str(Average_weight())
    filehandler.write(data)

    def Heat_map_creator():
        Cordinates_dictionary = Cells_centers_dict()
        Value_dictionary = Average_weight()
        Heat_map_dictionary = {}
        for keys in Cordinates_dictionary:
            Cordinates = Cordinates_dictionary[keys]
            Value = Value_dictionary[keys]
            Cordinates.append(Value)
            Heat_map_dictionary[keys] = Cordinates
        return Heat_map_dictionary


    filehandler = open('filename5.txt', 'wt')
    data = str(Heat_map_creator())
    filehandler.write(data)

    return Heat_map_creator()
# slownik = Cells_centers_dict()
# for keys in slownik:
#     operator = slownik[keys]
#     plt.scatter(operator[0], operator[1], s=1)

# plt.scatter(X, Y, s=0.5)
# plt.vlines(x = X_lines(X_cells_horizontal), ymin = Y_min, ymax = Y_max)
# plt.hlines(y = Y_lines(Y_cells_vertical), xmin = X_min, xmax = X_max)
# plt.show()
