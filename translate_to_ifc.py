"""A program to create objects out of an Ifc-class."""

"""Creation of the class PipeSegment with attributes."""

from import_from_csv import get_value, data, get_list

"""IfcPipeSegment"""


class PipeSegment(object):
    # Attribute definition
    File_Name = ""
    Object_Name = ""
    Object_Id = ""
    IFC_Element = ""
    Outer_Radius = ""
    Inner_Radius = ""
    Pipe_Usage = ""
    Pipe_type = ""
    Material = ""
    Length = ""
    X_start = ""
    Y_start = ""
    Z_start = ""
    X_end = ""
    Y_end = ""
    Z_end = ""
    Direction = ""
    Project = ""
    Building = ""
    Floor = ""
    Room = ""

    """Initialization of the attributes with a constructor."""

    # Constructor of the class (initializer)
    def __init__(self, File_Name, Object_Name, Object_Id, IFC_Element, Outer_Radius, Inner_Radius, Pipe_Usage,
                 Pipe_type,
                 Material, Length, X_start, Y_start, Z_start, X_end, Y_end, Z_end, Direction, Project, Building, Floor,
                 Room):
        self.File_Name = File_Name
        self.Object = Object_Name
        self.Object_Id = Object_Id
        self.IFC_Element = IFC_Element
        self.Outer_Radius = Outer_Radius
        self.Inner_Radius = Inner_Radius
        self.Pipe_Usage = Pipe_Usage
        self.Pipe_type = Pipe_type
        self.Material = Material
        self.Length = Length
        self.X_start = X_start
        self.Y_start = Y_start
        self.Z_start = Z_start
        self.X_end = X_end
        self.Y_end = Y_end
        self.Z_end = Z_end
        self.Direction = Direction
        self.Project = Project
        self.Building = Building
        self.Floor = Floor
        self.Room = Room

    # Function to print out the data of the class
    def print_PipeSegment_abilities(self):
        print("File Name: ", self.File_Name)
        print("Object Name: ", self.Object_Name)
        print("Object-Id: ", self.Object_Id)
        print("IFC-Element: ", self.IFC_Element)
        print("Outer Radius: ", self.Outer_Radius)
        print("Inner Radius: ", self.Inner_Radius)
        print("Pipe-usage: ", self.Pipe_Usage)
        print("Pipe-type: ", self.Pipe_type)
        print("Material: ", self.Material)
        print("Length: ", self.Length)
        print("X-Start: ", self.X_start)
        print("Y-Start: ", self.Y_start)
        print("Z-Start: ", self.Z_start)
        print("X-End: ", self.X_end)
        print("Y-End: ", self.Y_end)
        print("Z-End: ", self.Z_end)
        print("Direction: ", self.Direction)
        print("Project: ", self.Project)
        print("Building: ", self.Building)
        print("Floor: ", self.Floor)
        print("Room: ", self.Room)


"""Function to create objects out of the class."""


def create_PipeSegment(File_Name, Object_Name, Object_Id, IFC_Element, Outer_Radius, Inner_Radius, Pipe_Usage,
                       Pipe_type,
                       Material, Length, X_start, Y_start, Z_start, X_end, Y_end, Z_end, Direction, Project, Building,
                       Floor, Room):
    IfcPipe = PipeSegment(File_Name, Object_Name, Object_Id, IFC_Element, Outer_Radius, Inner_Radius, Pipe_Usage,
                          Pipe_type,
                          Material, Length, X_start, Y_start, Z_start, X_end, Y_end, Z_end, Direction, Project,
                          Building, Floor, Room)
    return IfcPipe


"""Loop to instantiate and save objects depending on csv data."""


x = 0
array = []

# Loop through lists of csv-data - one list is one object
for list in data[1:]:
    x = x + 1

    # Get values from csv-data to create objects and save them in an array
    array.append(create_PipeSegment(get_value(x, 0), get_value(x, 1), get_value(x, 2), get_value(x, 3),
                                    get_value(x, 4), get_value(x, 5), get_value(x, 6), get_value(x, 7),
                                    get_value(x, 8), get_value(x, 9), get_value(x, 10), get_value(x, 11),
                                    get_value(x, 12), get_value(x, 13), get_value(x, 14), get_value(x, 15),
                                    get_value(x, 16), get_value(x, 17), get_value(x, 18), get_value(x, 19),
                                    get_value(x, 20)))
print(array)


# class SimpleClass(object):
#    pass
# simplelist = []
# for count in xrange(4):
#    x = SimpleClass()
#    x.attr = count
#    simplelist.append(x)


## Instantiation - creating an object out of a class
# PipeValues = IfcPipeSegment(get_value(1, 0), get_value(1, 1), get_value(1, 2), get_value(1, 3),
#                                        get_value(1, 4), get_value(1, 5), get_value(1, 6), get_value(1, 7),
#                                        get_value(1, 8), get_value(1, 9), get_value(1, 10), get_value(1, 11),
#                                        get_value(1, 12), get_value(1, 13), get_value(1, 14), get_value(1, 15),
#                                        get_value(1, 16), get_value(1, 17), get_value(1, 18), get_value(1,19))


# PipeValues.print_IfcPipeSegment_abilities()

# objs = [IfcPipeSegment() for i in range(10)]
# for obj in objs:
#    IfcPipeSegment.add(obj)
#
# objs[0].print_IfcPipeSegment_abilities()
