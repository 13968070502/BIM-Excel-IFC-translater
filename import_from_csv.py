"""A file to import and write csv files."""

# Import csv file
import csv
path = 'data/Pipe_system.csv'

# Define headers
File_Name=0; Object=1; Object_Id=2; IFC_Element=3; Diameter=4; Elevation=5; Pipe_Usage=6; Pipe_type=7; X_min=8; Y_min=9; X_max=10; Y_max=11; Project=12; Building=13; Floor=14; Room=15

# Read csv
with open(path, 'r', newline='') as read_csv:

    # pass file objects to reader() to get the reader object
    csv_reader = csv.reader(read_csv, delimiter=';')

    # Pass reader object to list to get list of lists
    data = list(csv_reader)

# Print whole data
#for s in data:
#    print(*s)

def get_value(object, attribute):
    # Return specific value
    return data[object][attribute]






#for item in list_of_rows[0]:
#    print (item)
#    array.append([item + '=' + str(num)])
#    num += 1

#print (list_of_rows[3][1]) #Ausgabe Zeile 3 Header 1








#--------------------------------------------------------

#path = 'data\Input_Results_TGA_MASTER.csv'
#file = open(path, newline='')
#
## Read csv file
#with open(path, 'r') as Input_Results_TGA_MA:
#    csv_dict_reader = csv.DictReader(file, delimiter=';')
#    header = next(csv_dict_reader) # The first line is the header
#
#    for row in csv_dict_reader:
#        print(row)
#        print(header)


#------------------------------------------------------------
#
## Write new csv file
#
#newpath = 'data\Konverted_Input_Results_TGA_MA.csv'
#
#with open('data\Konverted_Input_Results_TGA_MA.csv', 'w', newline='') as Konverted_Input_Results_TGA_MA:
#
#    fieldnames = ['Object', 'Object_Id', 'IFC_Element']
#    csv_dict_writer = csv.DictWriter(Konverted_Input_Results_TGA_MA, fieldnames=fieldnames)
#    csv_dict_writer.writeheader()
#
#    for fieldnames in Konverted_Input_Results_TGA_MA:
#        csv_dict_writer.writerow(fieldnames)


#---------------------------------------------------------------------------


#    header = next(csv_dict_reader)  # The first line is the header
#    data.append([File_Name,Object,Object_Id,IFC_Element,Diameter,Material,Pipe_Color,Piping_type,H_V,Total_vertices,Xmin,Ymin,Xmax,Ymax,Project,Building,Floor,Room])


#with open('data/ExcelVorlage.csv', 'r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#
#    with open('data/ExcelVorlage_konv.csv', 'w') as new_file:
#        fieldnames = ['component', 'length', 'depth', 'height', 'material']
#
#        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#
#        csv_writer.writeheader()
#
#        for line in csv_reader:
#            csv_writer.writerow(line)