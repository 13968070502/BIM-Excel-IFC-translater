"""A program to create objects out of an Ifc-class."""

from import_from_csv import get_value


"""IfcPipeSegment"""


class IfcPipeSegment:
    # Attribute definition
    File_Name = ""
    Object = ""
    Object_Id = ""
    IFC_Element = ""
    Outer_Radius = ""
    Inner_Radius = ""
    Pipe_Usage = ""
    Pipe_type = ""
    Material = ""
    X_start = ""
    Y_start = ""
    Z_start = ""
    X_end = ""
    Y_end = ""
    Z_end = ""
    Project = ""
    Building = ""
    Floor = ""
    Room = ""

    # Constructor of the class
    def __init__(self, File_Name, Object, Object_Id, IFC_Element, Outer_Radius, Inner_Radius, Pipe_Usage, Pipe_type,
                 Material, X_start, Y_start, Z_start, X_end, Y_end, Z_end, Project, Building, Floor, Room):
        self.File_Name = File_Name
        self.Object = Object
        self.Object_Id = Object_Id
        self.IFC_Element = IFC_Element
        self.Outer_Radius = Outer_Radius
        self.Inner_Radius = Inner_Radius
        self.Pipe_Usage = Pipe_Usage
        self.Pipe_type = Pipe_type
        self.Material = Material
        self.X_start = X_start
        self.Y_start = Y_start
        self.Z_start = Z_start
        self.X_end = X_end
        self.Y_end = Y_end
        self.Z_end = Z_end
        self.Project = Project
        self.Building = Building
        self.Floor = Floor
        self.Room = Room

    # Function to print out the data of the class
    def print_IfcPipeSegment_abilities(self):
        print("File Name: ", self.File_Name)
        print("Object: ", self.Object)
        print("Object-Id: ", self.Object_Id)
        print("IFC-Element: ", self.IFC_Element)
        print("Outer Radius: ", self.Outer_Radius)
        print("Inner Radius: ", self.Inner_Radius)
        print("Pipe-usage: ", self.Pipe_Usage)
        print("Pipe-type: ", self.Pipe_type)
        print("Material: ", self.Material)
        print("X-Start: ", self.X_start)
        print("Y-Start: ", self.Y_start)
        print("Z-Start: ", self.Z_start)
        print("X-End: ", self.X_end)
        print("Y-End: ", self.Y_end)
        print("Z-End: ", self.Z_end)
        print("Project: ", self.Project)
        print("Building: ", self.Building)
        print("Floor: ", self.Floor)
        print("Room: ", self.Room)


# Instantiation - creating an object out of a class
IfcPipeSegment = IfcPipeSegment(get_value(1,0), get_value(1, 1), get_value(1, 2), get_value(1, 3),
                                        get_value(1, 4), get_value(1, 5), get_value(1, 6), get_value(1, 7),
                                        get_value(1, 8), get_value(1, 9), get_value(1, 10), get_value(1, 11),
                                        get_value(1, 12), get_value(1, 13), get_value(1, 14), get_value(1, 15),
                                        get_value(1, 16), get_value(1, 17), get_value(1, 18))


IfcPipeSegment.print_IfcPipeSegment_abilities()



#class IfcPipeSegment(IfcFlowElement):

#    def __init__(self, GlobalId, Name, Description, ObjectType, IsTypedBy, ObjectPlacement, HasOpenings):
#        super(IfcDistributionElement, self).__init__(GlobalId, Name, Description, ObjectType, IsTypedBy,
#                                                     ObjectPlacement, HasOpenings)

#    def print_IfcPipeSegment_abilities(self):
#        super(IfcPipeSegment, self).print_IfcDistributionElement_abilities()


# Instantiation - creating an object out of a class

#PipeSegment = IfcPipeSegment(create_GUID(), get_value(1, 1), get_value(1, 2), get_value(1, 8), get_value(1,3), '0.0.0', 'No')

#PipeSegment.print_IfcPipeSegment_abilities()