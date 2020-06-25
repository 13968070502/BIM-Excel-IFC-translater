"""A file to import and write csv files."""

# Import csv file
import csv

path = 'data/Pipe_system_short.csv'

# Define headers
File_Name = 0; Object = 1; Object_Id = 2; IFC_Element = 3; Radius = 4; inner_Radius = 5; Elevation = 6; Pipe_Usage = 7; Pipe_type = 8; Material=9; X_start = 10; Y_start = 11; X_end = 12; Y_end = 13; Project = 14; Building = 15; Floor = 16; Room = 17

# Read csv
with open(path, 'r', newline='') as read_csv:
    # pass file objects to reader() to get the reader object
    csv_reader = csv.reader(read_csv, delimiter=';')

    # Pass reader object to list to get list of lists
    data = list(csv_reader)

# Change all necessary Columns to double


# Print whole data
for s in data:
    print(*s)


def get_value(object, attribute):
    # Return specific value
    return data[object][attribute]



# ---------------------------------------------------------------------

# for item in list_of_rows[0]:
#    print (item)
#    array.append([item + '=' + str(num)])
#    num += 1
