"""Contains the functionality to write the data out in step format."""

from import_from_csv import get_value
from create_timestamp import create_timestamp


def write_to_step(data):
    """Write data in step format."""


# Construction elements of STEP-file
iso = "ISO-10303-21;"
header = "HEADER;"
file_description = "FILE_DESCRIPTION ("
end_row = ");"
start_argument = "('"
end_argument = "'), "
next_row = '\n'
file_name = "FILE_NAME ("
file_schema = "FILE_SCHEMA (('"
endsec = "ENDSEC;"
data = "DATA;"
end_iso = "END-ISO-10303-21;"
timestamp = create_timestamp()
representation_type = "('ViewDefinition [DesignTransferView_V1]'), "
author = "Wellenhofer"
ifc_version = "IFC4"
implementation_level = "2;1"
no_value = "''"
no_value_b = "('')"
no_value_S = "$"
comma = ", "
apostrophe = "'"

# Imported Data from CSV-File


# Construction of STEP-File
with open('STEP-file.ifc', 'w') as f:
    # HEADER section
    f.write(iso + next_row)
    f.write(header + next_row)
    f.write(
        file_description + representation_type + apostrophe + implementation_level + apostrophe + end_row + next_row)
    f.write(
        file_name + no_value + comma + apostrophe + timestamp + apostrophe + comma + start_argument + author + end_argument + no_value_b + comma + no_value + comma + no_value + comma + no_value + end_row + next_row)
    f.write(file_schema + ifc_version + "')" + end_row + '\n')
    f.write(endsec + '\n')

    # DATA section
    f.write(data + '\n')

    # Placement with local coordinates:
    f.write("#101=IFCCARTESIANPOINT((0.000,0.000,0.000));" + next_row)  # origin point
    f.write("#102=IFCDIRECTION((1.000,0.000,0.000));" + next_row)  # x-axis
    f.write("#103=IFCDIRECTION((0.000,1.000,0.000));" + next_row)  # y-axis
    f.write("#104=IFCDIRECTION((0.000,0.000,1.000));" + next_row)  # z-axis
    f.write("#105=IFCAXIS2PLACEMENT3D(#101,#104,#102);" + next_row)  # cartesian coordinate system

    # Declaration of Units:
    f.write("#121=IFCSIUNIT($,.LENGTHUNIT.,$,.METRE.);" + next_row)  # cartesian point coordinates
    f.write("#122=IFCSIUNIT($,.PLANEANGLEUNIT.,$,.RADIAN.);" + next_row)  # rotation angles
    f.write("#123=IFCUNITASSIGNMENT((#121,#122));" + next_row)

    # Geometric representations:
    f.write("#142=IFCGEOMETRICREPRESENTATIONCONTEXT('3D body','3D-Models VR',3,$,#105,$);" + next_row)
    f.write("#145=IFCGEOMETRICREPRESENTATIONSUBCONTEXT('body300','LOD300',$,$,$,$,#142,$,.MODEL_VIEW.,$);" + next_row)

    # Assign contexts, units to project:
    f.write("#181=IFCPROJECT('2Dx3oA_r5F69i0DCABvXDv',$,'pipe project',$,$,$,$,(#145),#123);" + next_row)

    # 3D-Body-context:
    f.write("#201=IFCCARTESIANPOINT((0.000,0.300));" + next_row)  # x=0           , y=inner radius
    f.write("#202=IFCCARTESIANPOINT((0.000,0.400));" + next_row)  # x=0           , y=outer radius
    f.write("#203=IFCCARTESIANPOINT((5.000,0.400));" + next_row)  # x=length      , y=outer radius
    f.write("#204=IFCCARTESIANPOINT((5.000,0.300));" + next_row)  # x=length      , y=inner radius
    f.write("#205=IFCCARTESIANPOINT((0.000,0.300));" + next_row)
    f.write("#212=IFCPOLYLINE((#201,#202,#203,#204,#205));" + next_row)
    f.write("#213=IFCARBITRARYCLOSEDPROFILEDEF(.AREA.,$,#212);" + next_row)  # declare poly as area
    f.write("#214=IFCAXIS2PLACEMENT3D(#101,#104,#102);" + next_row)  # revolve-plane
    f.write("#215=IFCAXIS1PLACEMENT(#101,#102);" + next_row)  # rotation axis
    f.write("#216=IFCREVOLVEDAREASOLID(#213,#214,#215,6.283);" + next_row)  # how
    f.write("#217=IFCSHAPEREPRESENTATION(#145,'body300',$,(#216));" + next_row)  # as

    # product shape definition, placement and instancing:
    f.write("#501=IFCPRODUCTDEFINITIONSHAPE($,$,(#217));" + next_row)  # with
    f.write("#502=IFCLOCALPLACEMENT($,#105);" + next_row)  # where
    f.write("#503=IFCFLOWSEGMENT('3poERwXYL9lgTG8ACKJuNz',$,'pipe',$,$,#502,#501,$);" + next_row)  # what

    # Assign properties to pipe:
    f.write("#701=IFCPROPERTYSINGLEVALUE('DN',$,IFCREAL(400),$);" + next_row)
    f.write("#702=IFCPROPERTYSET('1FGilBX2j3hgY6Jx3rLKfz',$,'pipe-properties',$,(#701));" + next_row)
    f.write("#703=IFCRELDEFINESBYPROPERTIES('3GIJzeSVL6_x3rDzCQWlth',$,$,$,(#503),#702);" + next_row)

    # Assign elements to project:
    f.write("#901=IFCRELAGGREGATES('1l4J2aaDD0b9lNurr4uB78',$,$,$,#181,(#503));" + next_row)

    # End file
    f.write(endsec + next_row)
    f.write(end_iso + next_row)

step_file = ""

# Read lines in text file
with open('STEP-file.ifc', 'r') as f:
    for line in f:
        print(line)

# Read one line in text file
# with open('STEP-file.ifc', 'r') as f:
#    step_file += f.readline()


print(step_file)
