"""Contains the functionality to write the data out in step format."""

def write_to_step(data):
    """Write data in step format."""


#read and write data
#Constant text elements of an IFC-File in STEP-format

ISO = 'ISO-10303-21'
HEADER = 'HEADER;'
FILE_DESCRIPTION = 'FILE_DECRIPTION(();'
FILE_NAME = 'FILE_NAME();'
FILE_SCHEMA = 'FILE_SCHEMA ();'
ENDSEC = 'ENDSEC;'

DATA = 'DATA;'
END_ISO = 'END-ISO-10303-21;'

#construct STEP-File

# w = schreiben, r = lesen, a = append
with open('STEP-file.ifc', 'w') as f:
    f.write(ISO + '\n')
    f.write(HEADER + '\n')
    f.write(FILE_DESCRIPTION + '\n')
    f.write(FILE_NAME + '\n')
    f.write(FILE_SCHEMA + '\n')
    f.write(ENDSEC + '\n')
    f.write(DATA + '\n')
    f.write(END_ISO+ '\n')

step_new = ""

with open('STEP-file.ifc', 'r') as f:
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()
    step_new += f.readline()

print(step_new)