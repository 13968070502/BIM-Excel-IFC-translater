"""A file to import and write csv files."""
# Import csv file

import csv
path = 'data\Input_Results_TGA_MASTER.csv'
num = 0
array = []

with open(path, 'r', newline='') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj, delimiter=';')
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

for s in list_of_rows:
    print(*s)

for item in list_of_rows[0]:
    print (item)
    array.append([item + '=' + str(num)])
    num += 1

print (array)

Object=0; Object_Id=1; IFC_Element=2; Diameter=3

print (list_of_rows[3][1])








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