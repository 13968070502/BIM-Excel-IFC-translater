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
X_start = 9
Y_start = 10
Z_start = 11
X_end = 12
Y_end = 13
Z_end = 14
Direction = 15
Project = 16
Building = 17
Floor = 18
Room = 19


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
