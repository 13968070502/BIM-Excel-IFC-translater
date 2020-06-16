"""A file to import csv files."""

import csv


path = "data\Input_Results_TGA_MA.csv"
file = open(path, newline= '')
reader = csv.reader(file, delimiter=';')

header = next(reader) # The first line is the header
data = [row for row in reader] # Read the remaining data

sort = sorted(reader, key=operator.itemgetter(0))


















#for row in reader:
#
#    File_Name = str(row[0])
#    Object = str(row[1])
#    Object_Id = str(row[2])
#    IFC_Element = str(row[3])
#    Diameter = str(row[4])
#    Material = str(row[5])
#    Pipe_Color = str(row[6])
#    Piping_type = str(row[7])
#    H_V = str(row[8])
#    Total_vertices = str(row[9])
#    Xmin = str(row[10])
#    Ymin = str(row[11])
#    Xmax = str(row[12])
#    Ymax = str(row[13])
#    Project = str(row[14])
#    Building = str(row[15])
#    Floor = str(row[16])
#    Room = str(row[17])


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