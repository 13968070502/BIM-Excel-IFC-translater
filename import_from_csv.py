"""A file to import and write csv files."""

# Import csv file
import csv

path = 'data/Pipe_system_short.csv'

# Define headers
File_Name = 0
Object_Name = 1
Object_Id = 2
IFC_Element = 3
Outer_Radius = 4
Inner_Radius = 5
Pipe_Usage = 6
Pipe_type = 7
Material = 8
Length = 9
X_start = 10
Y_start = 11
Z_start = 12
X_end = 13
Y_end = 14
Z_end = 15
Direction = 16
Project = 17
Building = 18
Floor = 19
Room = 20


# Read csv
with open(path, 'r', newline='') as read_csv:
    # pass file objects to reader() to get the reader object
    csv_reader = csv.reader(read_csv, delimiter=';')

    # Pass reader object to list to get list of lists
    data = list(csv_reader)


def get_value(object, attribute):
    # Return specific value
    return data[object][attribute]


def get_list(object):
    # Return specific list/object
    return data[object]

# ---------------------------------------------------------------------

# Print whole data
for s in data:
    print(*s)


#for item in data[0]:
#    print(item)
#    array.append([item + '=' + str(num)])
#    num += 1


# Change str to double/float
# print(type(float(get_value(3,9))))
# print(float(get_value(3,9)))
