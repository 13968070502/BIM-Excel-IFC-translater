"""A file to import and write csv files."""

# Import csv file
import csv

path = 'data/Pipe_system_short.csv'

# Define headers
File_Name = 0; Object = 1; Object_Id = 2; IFC_Element = 3; Outer_Radius = 4; Inner_Radius = 5; Pipe_Usage = 6; Pipe_type = 7; Material=8; X_start = 9; Y_start = 10; Z_start=11; X_end = 12; Y_end = 13; Z_end=14; Project = 15; Building = 16; Floor = 17; Room = 18

# Read csv
with open(path, 'r', newline='') as read_csv:
    # pass file objects to reader() to get the reader object
    csv_reader = csv.reader(read_csv, delimiter=';')

    # Pass reader object to list to get list of lists
    data = list(csv_reader)

# Change all necessary Columns to double


# Print whole data
#for s in data:
#    print(*s)


def get_value(object, attribute):
    # Return specific value
    return data[object][attribute]


# ---------------------------------------------------------------------

# for item in list_of_rows[0]:
#    print (item)
#    array.append([item + '=' + str(num)])
#    num += 1
