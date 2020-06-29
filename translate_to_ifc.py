"""A program to create objects out of an Ifc-class."""

from import_from_csv import get_value

# csv - headers
File_Name = 0;
Object = 1;
Object_Id = 2;
IFC_Element = 3;
Outer_Radius = 4;
Inner_Radius = 5;
Pipe_Usage = 6;
Pipe_type = 7;
Material = 8;
X_start = 9;
Y_start = 10;
Z_start = 11;
X_end = 12;
Y_end = 13;
Z_end = 14;
Project = 15;
Building = 16;
Floor = 17;
Room = 18

"""IfcPipeSegment"""


class IfcPipeSegment:
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
        print("File Name: "), self.File_Name
        print("Object: "), self.Object
        print("Object-Id: "), self.Object_Id
        print("IFC-Element: "), self.IFC_Element
        print("Outer Radius: "), self.Outer_Radius
        print("Inner Radius: "), self.Inner_Radius
        print("Pipe-usage: "), self.Pipe_Usage
        print("Pipe-type: "), self.Pipe_type
        print("Material: "), self.Material
        print("X-Start: "), self.X_start
        print("Y-Start: "), self.Y_start
        print("Z-Start: "), self.Z_start
        print("X-End: "), self.X_end
        print("Y-End: "), self.Y_end
        print("Z-End: "), self.Z_end
        print("Project: "), self.Project
        print("Building: "), self.Building
        print("Floor: "), self.Floor
        print("Room: "), self.Room


# Instantiation - creating an object out of a class
PipeSegment = IfcPipeSegment(File_Name, Object, Object_Id, IFC_Element, Outer_Radius, Inner_Radius, Pipe_Usage, Pipe_type,
                 Material, X_start, Y_start, Z_start, X_end, Y_end, Z_end, Project, Building, Floor, Room)
PipeSegment.print_IfcPipeSegment_abilities()
