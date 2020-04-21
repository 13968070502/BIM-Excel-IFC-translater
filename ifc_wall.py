# Classes
# Class "wall" with some abilities

class IfcWall:

    """Abilities of the Class"""
    GlobalId = "Wall.001"
    Name = "Wall"
    Description = "vertical construction that bounds or subdivides spaces"
    ObjectType = "Component"
    isTypedBy = "IfcBuildingElement"
    ObjectPlacement = 0.0
    HasOpenings = "Yes"
    length = 5.0
    width = 0.2
    height = 3.0

    # self bezieht sich immer auf die aktuelle Instanz
    # Konstruktor immer mit 2 Unterstrichen __

    """Definition des Konstruktors"""
    def __init__(self, GlobalId="Wall001", Name="Wand", Description="vertical construction that bounds or subdivides spaces", ObjectType="Component",
    isTypedBy="IfcBuildingElement", ObjectPlacement=0.0, HasOpenings="Yes", length=5.0, width=0.2, height=3.0): # muss immer definiert werden

       # hier werden die Begriffe für __init__ Konstruktor definiert
        self.GlobalId = GlobalId
        self.Name = Name
        self.Description = Description
        self.ObjectType = ObjectType
        self.isTypedBy = isTypedBy
        self.ObjectPlacement = ObjectPlacement
        self.HasOpenings = HasOpenings
        self.length = length
        self.width = width
        self.height = height

    """Definition der Ausgabe"""
    def printWallAbilitys(self):
        print('GlobalID: ',self.GlobalId)
        print('Name: ', self.Name)
        print('Description: ', self.Description)
        print('ObjectType: ', self.ObjectType)
        print('Is typed by: ', self.isTypedBy)
        print('Object Placement: ', self.ObjectPlacement)
        print('Has Openings: ', self.HasOpenings)
        print('Length: ', self.length)
        print('Width: ', self.width)
        print('Height: ', self.height)

WallData = IfcWall("Wall.001", "Wall", "vertical construction that bounds or subdivides spaces", "Component", "IfcBuildingElement", 0.0, "Yes", 5.0, 0.2, 3.0)
WallData.printWallAbilitys()