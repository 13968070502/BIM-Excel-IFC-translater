"""Contains the functionality to write the data out in step format."""

from import_from_csv import get_value
from create_timestamp import create_timestamp


def write_to_step(data):
    """Write data in step format."""


# Construction elements of STEP-file
iso = "ISO-10303-21"
header = "HEADER;"
file_description = "FILE_DESCRIPTION (("
end_row = ");"
end_ = '), '
next_row = '\n'
file_name = "FILE_NAME ("
file_schema = "FILE_SCHEMA (('"
endsec = "ENDSEC;"
data = "DATA;"
end_iso = "END-ISO-10303-21;"
timestamp = create_timestamp()
author = "Wellenhofer"
ifc_version = "IFC4"
implementation_level = "2;1"
no_value = "''"
no_value_b = "('')"
no_value_S = "$"
comma = ","
apostrophe = "'"

# Imported Data from CSV-File


# Construction of STEP-File
with open('STEP-file.ifc', 'w') as f:
    # HEADER section
    f.write(iso + next_row)
    f.write(header + next_row)
    f.write(file_description + apostrophe + get_value(1, 0) + apostrophe +    " ), '" + implementation_level + apostrophe + end_row + next_row)
    f.write(file_name + "'', '" + timestamp + "', ('" + author + "'), (''), '', '', ''" + end_row + next_row)
    f.write(file_schema + ifc_version + "')" + end_row + '\n')
    f.write(endsec + '\n')

    # DATA section
    f.write(data + '\n')

    # Placement with local coordinates:

    # Declaration of Units:

    # Geometric representations:

    # Assign global coordinates to 3D representation context:

    # Assign contexts, units to project:

    # 3D-Body-context:

    # product shape definition, placement and instancing:

    # Assign properties to pipe:

    # Assign elements to project:

    f.write(endsec + '\n')
    f.write(end_iso + '\n')

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
