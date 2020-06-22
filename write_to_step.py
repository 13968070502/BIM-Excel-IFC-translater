"""Contains the functionality to write the data out in step format."""

from step.time_stamp import create_timestamp

def write_to_step(data):
    """Write data in step format."""


# Constant text elements of an IFC-File in STEP-format
ISO = 'ISO-10303-21'
HEADER = 'HEADER;'
FILE_DESCRIPTION = 'FILE_DESCRIPTION(('
END_ROW = ');'
FILE_NAME = 'FILE_NAME('
FILE_SCHEMA = 'FILE_SCHEMA ('
ENDSEC = 'ENDSEC;'
DATA = 'DATA;'
END_ISO = 'END-ISO-10303-21;'

# Data created by Python
TIMESTAMP = create_timestamp()
AUTHOR = 'Wellenhofer'
IFC_VERSION = 'IFC4'
IMPLEMENTATION_LEVEL = '2;1'


# Imported Data from CSV-File




# Construction of STEP-File
with open('STEP-file.ifc', 'w') as f:
    f.write(ISO + '\n')
    f.write(HEADER + '\n')
    f.write(FILE_DESCRIPTION + END_ROW + '\n')
    f.write(FILE_NAME + TIMESTAMP + END_ROW + '\n')
    f.write(FILE_SCHEMA + END_ROW + '\n')
    f.write(ENDSEC + '\n')
    f.write(DATA + '\n')

    # Placement with local coordinates:

    # Declaration of Units:

    # Geometric representations:

    # Assign global coordinates to 3D representation context:

    # Assign contexts, units to project:

    # 3D-Body-context:

    # product shape definition, placement and instancing:

    # Assign properties to pipe:

    # Assign elements to project:


    f.write(ENDSEC + '\n')
    f.write(END_ISO + '\n')

step_file = ""

with open('STEP-file.ifc', 'r') as f:
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()
    step_file += f.readline()


print(step_file)
